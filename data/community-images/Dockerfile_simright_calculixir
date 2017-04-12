FROM daocloud.io/debian:jessie

MAINTAINER Wells Jia <wells.jia@simright.com>

VOLUME data

RUN apt-get update \
    && apt-get install -y gfortran wget curl \
    && wget -O /etc/apt/sources.list https://raw.githubusercontent.com/opensource-yunnan-university/source_automate/master/ubuntu/sources.list.ynu.16.04 \ 
    && mkdir -p /calculixir 

WORKDIR /calculixir

ADD ./calculix_2.11.tar.gz /calculixir 


ENTRYPOINT ["./calculix_2.11/bin/ccx"]
