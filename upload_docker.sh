#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=tictactoeserver .


dockerpath="eareyan/tictactoeserver"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag tictactoeserver $dockerpath

# Push Image
docker image push $dockerpath