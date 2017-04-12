FROM ubuntu:14.04 

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.ide.name="Docker Compose" org.kurron.ide.version=1.7.0

RUN apt-get update && \
    apt-get install -y curl ca-certificates && \
    curl -L https://github.com/docker/compose/releases/download/1.7.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

RUN chmod 0555 /usr/local/bin/*

VOLUME ["/home/developer"]
VOLUME ["/pwd"]

ENV HOME /home/developer
WORKDIR /pwd
ENTRYPOINT ["/usr/local/bin/docker-compose"]
CMD ["--version"]
