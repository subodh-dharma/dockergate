############################################################
# Dockerfile to build OpenTTD container images
# Based on phusion:baseimage (from ubuntu)
############################################################
FROM phusion/baseimage:latest
MAINTAINER Anrdrei Nadejde <andrei.nadejde@gmail.com>

ARG OPENTTD_VERSION="1.6.1-RC1"
ARG OPENGFX_VERSION="0.5.4"

ADD . /tmp
RUN /tmp/prepare.sh && \
    /tmp/system_services.sh && \
    /tmp/cleanup.sh

VOLUME /home/openttd/.openttd

EXPOSE 3001/tcp
EXPOSE 3001/udp
EXPOSE 6001/tcp
EXPOSE 6001/udp
