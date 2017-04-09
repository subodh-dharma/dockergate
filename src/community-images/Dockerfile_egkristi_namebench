FROM ubuntu:16.04
MAINTAINER Erling G. M. Kristiansen <egkristi@gmail.com>

# set env vars
ENV container docker
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

# configure apt behaviour
RUN echo "APT::Get::Install-Recommends 'false'; \n\
  APT::Get::Install-Suggests 'false'; \n\
  APT::Get::Assume-Yes "true"; \n\
  APT::Get::force-yes "true";" > /etc/apt/apt.conf.d/00-general

# systemd tweaks
RUN rm -rf /lib/systemd/system/getty*;

# install
RUN apt-get update
RUN apt-get install -y apt-utils

# install namebench
RUN apt-get install -y namebench

# install typical requirements for testing
RUN apt-get install -y procps ssl-cert ca-certificates apt-transport-https python sudo curl net-tools vim iproute unzip vim wget

# cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# finally run script on startup
CMD ["/bin/bash"]
