FROM jenkins:latest

USER root
# Connect apt docker repo
RUN apt-get update && apt-get install -y apt-transport-https sudo && \
    apt-get purge docker.io* && \
    apt-get autoclean && apt-get autoremove && \
    apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo "deb https://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list

# Install Docker and Docker Compose
RUN apt-get update && apt-get install -y docker-engine && apt-get autoclean && apt-get autoremove
RUN curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Configure docker group and jenkins user
RUN usermod -aG docker jenkins && usermod -aG sudo jenkins && id jenkins
RUN echo "jenkins ALL=(ALL)	NOPASSWD: ALL" >> /etc/sudoers

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

# Connect git-lfs repo
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash

# Install rsync and git-lfs
RUN apt-get update && apt-get install -y rsync git-lfs && apt-get autoclean && apt-get autoremove

USER jenkins
RUN git lfs install

EXPOSE 8080
