#Basic image with Spark 2.0 , JDK8 and Python 2.7 +numpy
#Meant to be used with Spark out-of-box project: github.com/athosgvag/spark_out-of-box
FROM debian:7.11
MAINTAINER Gustavo Castilhos <gustavo.vc.13@gmail.com>

ENV JAVA_HOME=/usr/java/jdk1.8.0_45 PATH=$PATH:/usr/java/jdk1.8.0_45/bin:/etc/spark-2.0.0-bin-hadoop2.7/bin SPARK_HOME=/etc/spark-2.0.0-bin-hadoop2.7
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install wget python-numpy \
 && wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz" \
 && mkdir -p /usr/java \
 && tar -xzf jdk-8u45-linux-x64.tar.gz -C /usr/java/ \
 && rm jdk-8u45-linux-x64.tar.gz \
 && wget http://www-us.apache.org/dist/spark/spark-2.0.0/spark-2.0.0-bin-hadoop2.7.tgz \
 && tar zxvf spark-2.0.0-bin-hadoop2.7.tgz -C /etc \
 && rm spark-2.0.0-bin-hadoop2.7.tgz \
 && sed 's/log4j.rootCategory=INFO, console/log4j.rootCategory=ERROR, console/g' $SPARK_HOME/conf/log4j.properties.template > $SPARK_HOME/conf/log4j.properties \
 && apt-get -y install procps
