FROM ubuntu:16.04

MAINTAINER Houzard Jean-François <jhouzard@gmail.com>

ENV MAVEN_VERSION=3.2.3
ENV JAVA_VERSION_MAJOR=7
ENV JAVA_VERSION_MINOR=79
ENV JAVA_VERSION_BUILD=15

ENV TZ=Europe/Luxembourg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# update dpkg repositories
RUN apt-get update \
 && apt-get install -y wget \
 && apt-get clean

# Install maven
RUN wget --no-verbose -O /tmp/apache-maven-${MAVEN_VERSION}.tar.gz http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
 && tar xzf /tmp/apache-maven-${MAVEN_VERSION}.tar.gz -C /opt/ \
 && ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven \
 && rm -f /tmp/apache-maven-${MAVEN_VERSION}.tar.gz

# Update settings.xml
# Externalise repository?

ENV MAVEN_HOME /opt/maven

# set shell variables for java installation
ENV java_version 1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
ENV filename jdk-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
ENV downloadlink http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/$filename

# unpack java
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/$filename $downloadlink \
 && tar -zxf /tmp/$filename -C /opt/ \
 && rm /tmp/$filename \
 && mv opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/oracle-jdk-1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} \
 && ln -s /opt/oracle-jdk-1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/java

ENV JAVA_HOME /opt/java
ENV PATH $JAVA_HOME/bin:$MAVEN_HOME/bin:$PATH

COPY settings.xml /opt/maven/conf
