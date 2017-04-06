# Base CentOS 7 with a few perks
# Includes epel repo for local build

FROM centos:latest

MAINTAINER Andre Fernandes

# You can edit the repo file and uncomment the lines below
# in order to use a local CentOS-Base mirror (if you have one).
# This is HIGHLY recommended if you plan to build
# images locally.

# ADD CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo

# Disabling the fastest mirror plugin is also a good
# idea if you have a local mirror.

# RUN sed -i 's/enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf

RUN yum update -y && yum install net-tools tar wget unzip -y && yum clean all && \
    yum install epel-release -y && \
    yum repolist && \
    yum install pwgen -y && \
    yum clean all

