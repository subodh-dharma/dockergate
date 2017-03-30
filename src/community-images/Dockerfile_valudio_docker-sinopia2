FROM node
MAINTAINER Valudio <development@valudio.com>
RUN adduser --disabled-password --gecos "" sinopia
RUN mkdir -p /opt/sinopia/storage
WORKDIR /opt/sinopia
RUN npm install js-yaml sinopia2
RUN chown -R sinopia:sinopia /opt/sinopia
USER sinopia
ADD /config.yaml /tmp/config.yaml
ADD /start.sh /opt/sinopia/start.sh
CMD ["sh", "/opt/sinopia/start.sh"]
EXPOSE 4873
VOLUME /opt/sinopia