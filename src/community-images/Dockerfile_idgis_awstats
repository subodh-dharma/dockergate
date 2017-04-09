FROM ubuntu:14.04

RUN apt-get -y update && \
	apt-get install -y \
		apache2 \
		awstats \
		gettext

COPY awstats.stats.conf /etc/awstats/awstats.stats.conf.template
COPY run.sh /

ENV AWSTATS_CONF_LOGFILE="/var/log/apache2/other_vhosts_access.log"
ENV AWSTATS_CONF_LOGFORMAT="%referer %host %logname %other %time1 %methodurl %code %bytesd %refererquot %uaquot"
ENV AWSTATS_CONF_SITEDOMAIN="awstats"

WORKDIR /

RUN a2enmod cgi

EXPOSE 80

CMD /run.sh
