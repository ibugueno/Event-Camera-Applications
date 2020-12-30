import math
import itertools    
from itertools import groupby

from dv import AedatFile
from dv import LegacyAedatFile
import numpy as np
import time

import os
import shutil

window_time = 0.1 #ms

def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    result = ([e for e in t if e != None] for t in itertools.zip_longest(*args))    

    return list(result)

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def get_time_classes(annotation_f):

    a_file = open(annotation_f, 'r')
    next(a_file)
            
    counter = 0
    t = 0

    all_samples = []

    for l in a_file:

        if (t%100 == 0):
            all_samples.append(t)

        l = l.replace('\n', '')

        all_samples.append(l)

        counter += 1
        t = int(counter*(1000/30))

    all_samples = mygrouper(4, all_samples)
    all_samples = list(all_samples)

    time_classes = []

    for sample in all_samples:
        t = sample[0]
        classes = sample[1:]

        if (all_equal(classes)):
            time_classes.append([t/1000, sample[1]])

    return time_classes

def get_v2e_dvs_events(data_f):
    with LegacyAedatFile(data_f) as f:
        v2e_dvs_events = []
        for event in f:

            t = (event.timestamp)/1e6
            x = 345 - event.x
            y = 194 - event.y
            p = 1 if event.polarity else -1

            v2e_dvs_events.append([x, y, t, p])
    return v2e_dvs_events

def generate_numpy(target_path, list_1, list_2):
    list_numpy = []

    i = 0
    counter = [0, 0, 0, 0, 0, 0, 0]

    for l1 in list_1:
        ti = l1[0]
        tf = l1[0] + 0.1
        class_id = l1[1]

        i = 0
        for l2 in list_2:

            l2_t = l2[2]

            if (l2_t >= ti):
                if (l2_t < tf):
                    list_numpy.append(l2)
                    i = i + 1

                else:
                    list_2 = list_2[i:]

                    np.save(target_path + 'numpy/' + class_id +  '/' + class_id + '_' + str(counter[int(class_id)]) + '.npy', np.array(list_numpy) )
                    list_numpy = []

                    counter[int(class_id)] += 1

                    break


def numpy_folders(target_path):
    try:
        shutil.rmtree(target_path + 'numpy')
    except: 
        print('Directory doesnt exist')
    
    access_rights = 0o777
    os.mkdir(target_path + 'numpy', access_rights)
    
    for a in range(0, 7):
        os.mkdir(target_path + 'numpy/' + str(a), access_rights)


def check_dimensions(target_path, f):

    output_height = False
    output_width = False

    with open(target_path + f + '/v2e-args.txt') as v2eargs:
        for line in v2eargs:
            #print(line)
            
            if ('output_height' in line and '195' in line):
                output_height = True
                
            if ('output_width' in line and '346' in line and output_height):
                output_width = True
                #break        
                
    return (output_height and output_width)
        
if __name__ == "__main__":

    target_path = 'Train_Set/'

    numpy_folders(target_path)

    print(target_path)
    folders = os.listdir(target_path)
    folders.remove('annotations')
    folders.remove('numpy')

    print(folders)

    for f in folders:
        
        aedat = target_path + f + '/data.aedat'
            
        indexes = [i for i, x in enumerate(os.listdir(target_path + 'annotations/')) if f in x]
        if (len(indexes) == 1):

            print('\n\n\n')
            print('f: ',f)
            print('target_path: ', target_path + f + '/data.aedat')
        
            print('')

            if (check_dimensions(target_path, f)):
                
                annotation = target_path + 'annotations/' + os.listdir(target_path + 'annotations/')[indexes[0]]
                
                print('aedat: ', aedat)
                print('annotation: ', annotation, '\n')
                
                list_1 = get_time_classes(annotation)
                print('get_time_classes ok')
                
                
                start_time = time.time()
                list_2 = get_v2e_dvs_events(aedat)
                print('get_v2e_dvs_events ok')
                print("--- %s seconds ---" % (time.time() - start_time))
                
                
                start_time = time.time()
                generate_numpy(target_path, list_1, list_2)
                print('generate_numpy ok')
                print("--- %s seconds ---" % (time.time() - start_time))
                
            else:
                print('pass')

