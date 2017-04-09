FROM ubuntu:14.04

MAINTAINER Tauve Tauvetech <"tauvetech@gmail.com">

#RUN echo -n 'Acquire::http::Proxy "http://10.255.100.11:3128";' > /etc/apt/apt.conf

#ENV http_proxy http://10.255.100.11:3128
#ENV https_proxy https://10.255.100.11:3128
#ENV ftp_proxy ftp://10.255.100.11:3128

#RUN apt-get update

ADD install_script_docker.sh /root
ADD orocos-dot-service_with_rtt-ros-integration.patch /root
ADD orocos-yarp-transport_with_rtt-ros-integration.patch /root

