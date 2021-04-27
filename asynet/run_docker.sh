#!/bin/bash

docker rm -fv ignacio_asynet_ncaltech

#nvidia-docker run -it -e NVIDIA_VISIBLE_DEVICES=0  --name ignacio_asynet_ncaltech -v /home/ignacio/Proyectos/UOH/data:/app/data ignacio_asynet_ncaltech
docker run -it --name ignacio_asynet_ncaltech -v /home/ignacio/Proyectos/UOH/data:/app/data ignacio_asynet_ncaltech

#sleep 10; docker logs ignacio_erl
