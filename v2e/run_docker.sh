#!/bin/bash

docker rm -fv ignacio_v2e

nvidia-docker run -it -e NVIDIA_VISIBLE_DEVICES=0  --name ignacio_v2e -v /home/ignacio.bugueno/cachefs/v2e/input:/app/input -v /home/ignacio.bugueno/cachefs/v2e/output:/app/output ignacio_v2e

sleep 10; docker logs ignacio_v2e
