#!/bin/bash

#docker rm -fv ignacio_affwild_np_clean_Train_100ms

nvidia-docker run -it -e NVIDIA_VISIBLE_DEVICES=0 --name ignacio_affwild_np_clean_Train_100ms -v /home/ignacio.bugueno/cachefs/erl/input:/app -v ignacio_affwild_np_clean_Train_100ms

#sleep 10; docker logs ignacio_affwild_np_clean_Train_100ms


#docker run -d -p 80:80 --name ignacio_affwild_np_clean_Train_100ms -P -v /home/ignacio/Proyectos/UOH/Event-Camera-Applications/erl_numpy:/app affwild_np 