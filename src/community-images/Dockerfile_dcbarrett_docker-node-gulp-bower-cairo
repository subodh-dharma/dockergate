FROM dockerfile/nodejs:latest

MAINTAINER Drew Barrett "drew-barrett@live.com"

RUN apt-get update
RUN apt-get install -y python-software-properties python build-essential curl libfreetype6 libfontconfig git-core
RUN apt-get install -y libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++
RUN npm install -g gulp phantomjs bower