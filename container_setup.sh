#!/bin/sh
DOCKER_HOST_IP=$(ipconfig getifaddr en0)
docker-compose up -d --build
docker-compose ps
