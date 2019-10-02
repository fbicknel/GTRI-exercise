#!/bin/bash

: ${PROJECT_ROOT:=/home/fbicknel/projects/GTRI}
cd $PROJECT_ROOT/docker
: ${IMAGE_NAME:=tika_image}

docker stop $(docker ps -a -q --filter="ancestor=${IMAGE_NAME}")
docker build --tag=${IMAGE_NAME} . && docker run -d -p 4242:4242 ${IMAGE_NAME} && \
    docker container prune --filter "until=2h" -f

