FROM debian:jessie

RUN apt-get update \
	&& apt-get install -y gcc make g++ zlib1g-dev tar git wget xz-utils socket \
    && apt-get -q -y clean 

RUN cd /tmp/ \
	&& wget http://www.fefe.de/libowfat/libowfat-0.30.tar.xz \
	&& tar -xpvf libowfat-0.30.tar.xz  \
	&& mv libowfat-0.30 libowfat \
	&& make -C /tmp/libowfat

RUN cd /tmp/ \
	&& find / -name 'socket.h' \
	&& git clone https://erdgeist.org/gitweb/opentracker \
	&& ls -lha /tmp \
	&& make -C /tmp/opentracker \
	&& ln -s /tmp/opentracker/opentracker /bin/opentracker

COPY opentracker.conf /etc/opentracker.conf
COPY entrypoint.sh /

EXPOSE 6969 80

ENTRYPOINT ["sh", "entrypoint.sh"]
