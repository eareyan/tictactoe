#!/usr/bin/env bash

# Build image
docker build --tag=tictactoeserver .

# List docker images
docker image ls

# Run flask app
docker run -p 8080:8080 tictactoeserver