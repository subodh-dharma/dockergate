FROM nginx
MAINTAINER Cyrille Nofficial<cynoffic@cyrilix.fr>

LABEL version="0.1"
LABEL description="Tiny Tiny RSS web-based news feed (RSS/Atom) reader/aggregator"

RUN     apt-get update &&\
        apt-get upgrade &&\
        apt-get -y install php5-fpm git - php5-pgsql php5-curl php5-gd php5-json

RUN  git clone https://tt-rss.org/git/tt-rss.git /opt/ttrss



COPY php-fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf
RUN  ln -s /opt/ttrss/config.php-dist /opt/ttrss/config.php
RUN  adduser --system --home /opt/ttrss ttrss
RUN  chown -R ttrss  /opt/ttrss/


WORKDIR /opt/ttrss
USER ttrss

EXPOSE 8080


CMD /usr/bin/php -q update.php -daemon && /usr/sbin/php5-fpm --no-php-ini --fpm-config /etc/php5/fpm/php-fpm.conf --nodaemonize
