# A container which runs nginx for Django, SSH, new relic.
FROM ubuntu:14.04

MAINTAINER Andres Riancho version: 0.1

# Remove some useless errors which appear when installing packages with apt
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Setup apt
RUN apt-get update

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update

# Install required packages
RUN apt-get install -y build-essential git joe openssh-server coreutils gzip \
                       python python-dev python-setuptools wget ca-certificates \
                       nginx supervisor libssl-dev curl rsyslog

# Build dependencies
RUN easy_install pip==1.4.1
RUN pip install --upgrade pip==1.4.1

# Install new relic
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >> /etc/apt/sources.list.d/newrelic.list
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -
RUN apt-get update
RUN apt-get install newrelic-sysmond

# install uwsgi now because it takes a little while
RUN pip install uwsgi==2.0

# Configure SSH
RUN mkdir -p /var/run/sshd
RUN useradd docker --shell /bin/bash --create-home
WORKDIR /home/docker/

# Adding custom/local SSH key so the docker user can login
RUN mkdir /home/docker/.ssh/
RUN touch /home/docker/.ssh/authorized_keys
RUN pip install ssh-import-id==3.19

RUN chown docker: -R /home/docker/.ssh/
RUN chmod 700 /home/docker/.ssh/
RUN chmod 600 /home/docker/.ssh/authorized_keys

# Basic nginx configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

# We trust github's SSH
RUN ssh-keyscan -H github.com > /etc/ssh/ssh_known_hosts

# Workaround for log error
# https://bugs.launchpad.net/ubuntu/+source/rsyslog/+bug/830046
RUN rm -rf /etc/rsyslog.d/50-default.conf
RUN ln -s /home/docker/base/config/50-default.conf /etc/rsyslog.d/

# Workaround for log error
# https://bugs.launchpad.net/ubuntu/+source/sudo/+bug/155794
RUN touch /etc/default/locale

# TODO: Disable imklog for now, re-enable it later! Will be important to debug OOM
RUN sed -i 's/$ModLoad imklog/#$ModLoad imklog/' /etc/rsyslog.conf
RUN sed -i 's/$KLogPermitNonKernelFacility/#$KLogPermitNonKernelFacility/' /etc/rsyslog.conf

# copy our code
ADD . /home/docker/base/
WORKDIR /home/docker/base/

# Save the revision so we can easily know which base image was used to create
# our final docker image
RUN git rev-parse --short HEAD > git-revision

RUN rm -rf .git/
RUN rm -rf .gitignore

RUN ln -s /home/docker/base/config/nginx.conf /etc/nginx/sites-enabled/

# We want supervisord to run nginx and celery
RUN ln -s /home/docker/base/config/supervisord-nginx.conf /etc/supervisor/conf.d/
RUN ln -s /home/docker/base/config/supervisord-uwsgi.conf /etc/supervisor/conf.d/
RUN ln -s /home/docker/base/config/supervisord-sshd.conf /etc/supervisor/conf.d/
RUN ln -s /home/docker/base/config/supervisord-newrelic.conf /etc/supervisor/conf.d/
RUN ln -s /home/docker/base/config/supervisord-rsyslog.conf /etc/supervisor/conf.d/

# Cleanup to reduce image size
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/pip-build-root

# I want the web application running in the container to be accessible from
# the outside. We're exposing a REST API to control and monitor the scan worker
EXPOSE 80
EXPOSE 22

# RUN supervisord with our configuration so that the daemons are started
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
