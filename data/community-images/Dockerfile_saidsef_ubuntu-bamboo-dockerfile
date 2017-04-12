FROM alpine:latest
MAINTAINER Said Sef <said@saidsef.co.uk>

LABEL version="4.0"
LABEL description="Containerised Bomboo Server"

ENV BB_PKG_NAME atlassian-bamboo-5.13.2
ENV PATH /opt/$BB_PKG_NAME/bin:$PATH
ENV HOME /tmp

# Define working directory.
WORKDIR /data

# Install OpenJDK 8
RUN apk add --update wget curl openjdk8-jre-base

# Install Bamboo
RUN echo $BB_PKG_NAME
RUN wget https://my.atlassian.com/software/bamboo/downloads/binary/$BB_PKG_NAME.tar.gz
RUN tar xvzf $BB_PKG_NAME.tar.gz
RUN rm -vf $BB_PKG_NAME.tar.gz
RUN mkdir -p /opt
RUN mv $BB_PKG_NAME /opt

# Clean up
RUN rm -rf /var/cache/apk/*

# Define mountable directories
VOLUME ["/data"]

# ADD  bamboo-init.properties config
ADD config/bamboo-init.properties /opt/$BB_PKG_NAME/WEB-INF/classes/bamboo-init.properties

#  create build id
ARG BUILD_ID=""
RUN echo ${BUILD_ID} > build_id.txt

# Expose ports
EXPOSE 8085

# Define default command.
CMD ["/opt/"$BB_PKG_NAME"/bin/start.sh"]
