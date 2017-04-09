FROM ruby:2.3
MAINTAINER nacanori@gmail.com

ENV NVM_DIR /usr/local/nvm
ENV NVM_VERSION v0.33.0
ENV NODE_VERSION 6.9.1
ENV YARN_VERSION 0.16.1

# install mpdejs with nvm
RUN apt-get update
RUN curl https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default \
    && npm install --global yarn@$YARN_VERSION
