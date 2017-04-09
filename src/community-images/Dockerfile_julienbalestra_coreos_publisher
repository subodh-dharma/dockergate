FROM debian:latest

ADD requirements.txt /tmp/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    python-pip && \
     apt-get clean autoclean && \
     apt-get autoremove -y && \
     pip install -r /tmp/requirements.txt && \
     mkdir /opt/publisher

ADD s3_publisher.py /opt/publisher/s3_publisher.py

RUN chmod +x /opt/publisher/s3_publisher.py

WORKDIR /opt/publisher

ENTRYPOINT ["/opt/publisher/s3_publisher.py"]