FROM ubuntu:14.04.5
MAINTAINER ASCDC <ascdc@gmail.com>

ADD run.sh /run.sh

RUN DEBIAN_FRONTEND=noninteractive && \
	chmod +x /*.sh && \
	apt-get update && \
	apt-get -y dist-upgrade && \
	apt-get -y install vim curl git && \
	mkdir -p /var/www/mirador && \
	cd /var/www/mirador && \
	curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash && \
	export NVM_DIR="/root/.nvm" && \
	[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
	nvm install v6.1.0 && \
	nvm use v6.1.0 && \
	git clone https://github.com/ProjectMirador/mirador.git /var/www/mirador && \
	npm install -g grunt-cli && \
	npm install -g bower && \
	npm install && \
	bower install --allow-root 
	
WORKDIR /var/www/mirador
ENTRYPOINT ["/run.sh"]