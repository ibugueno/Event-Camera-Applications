from os import listdir
from os.path import isfile, join
from videoprops import get_video_properties
import math

import subprocess
import time


input_path = 'input/Test_Set/'
output_path = 'output/Test_Set/'
files = [f for f in listdir(input_path) if isfile(join(input_path, f))]


for file in files:

	input_full_path  = input_path + file
	output_full_path = output_path + file[:-4]

	props = get_video_properties(input_full_path)

	print(f'''Resolution: {props['width']}×{props['height']}''')

	new_w = 346
	new_h = math.ceil((new_w * props['height'])/props['width'])

	print(f'''New resolution: {new_w}×{new_h}''')

	start_time = time.time()
	subprocess.call('./run_v2e.sh ' + input_full_path + ' ' + output_full_path + ' ' + str(new_w) + ' ' + str(new_h), shell=True)
	print("--- %s seconds ---" % (time.time() - start_time))

	print('\n')

