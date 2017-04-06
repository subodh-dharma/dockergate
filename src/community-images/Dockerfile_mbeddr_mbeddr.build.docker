FROM debian:jessie
MAINTAINER Kolja Dummann <kolja.dummann@logv.ws>
ADD ./backports.list /etc/apt/sources.list.d/backports.list
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get -t jessie-backports install -y openjdk-8-jdk && apt-get install -y \
	ant \
	build-essential \
	bison \
	ca-certificates \
	curl \
	flex \
	g++ \
	gcc \
	gdb \
	git \
	lcov \
	libz-dev \
	libwww-perl \
	libxerces-c-dev \
	make \
	g++-multilib \
	libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 \
	patch \
	subversion \
	supervisor \
	unzip \
	wget \
	xvfb \
	zip

RUN apt-get autoremove
RUN cd /tmp && \
	wget https://github.com/aktau/github-release/releases/download/v0.6.2/linux-amd64-github-release.tar.bz2 && \
	tar -xjvf linux-amd64-github-release.tar.bz2 && \
	mv bin/linux/amd64/github-release /usr/bin/ && \
	rm -rf bin/

RUN \
	cmake_major_minor=3.7 && \
	cmake=cmake-${cmake_major_minor}.1-Linux-x86_64 && \
	cd /tmp && \
	wget https://cmake.org/files/v${cmake_major_minor}/${cmake}.tar.gz && \
	tar -xzvf ${cmake}.tar.gz && \
	cp -R ${cmake}/bin ${cmake}/share /usr && \
	rm -rf ${cmake} ${cmake}.tar.gz

RUN mkdir /buildAgent && cd /buildAgent && \
	wget https://build.mbeddr.com/update/buildAgent.zip && \
	unzip buildAgent.zip && \
	chmod +x /buildAgent/bin/agent.sh
ADD ./buildAgent.properties /buildAgent/conf/buildAgent.properties
ADD ./start.sh /start
RUN mkdir -p /root/.ssh /var/log/supervisor
ADD ./sshconfig /root/.ssh/config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod +x /start
CMD ["/usr/bin/supervisord"]
COPY ./bin/* /usr/bin/
RUN \
	wget http://spinroot.com/spin/Bin/spin646_linux64.gz && \
	gunzip spin646_linux64 && \
	mv spin646_linux64 /usr/bin/spin

# Install our own cppcheck because 1.67 in jessie is buggy
RUN \
	cppcheck_version=1.77 && \
	cd /tmp && \
	wget -O cppcheck-${cppcheck_version}.tar.gz https://github.com/danmar/cppcheck/archive/${cppcheck_version}.tar.gz && \
	tar -zxf cppcheck-${cppcheck_version}.tar.gz && \
	apt-get -y install libpcre3-dev && \
	(cd cppcheck-${cppcheck_version} && make install SRCDIR=build CFGDIR=/usr/share/cppcheck/cfg HAVE_RULES=yes CXXFLAGS="-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function") && \
	rm -rf cppcheck-${cppcheck_version}.tar.gz cppcheck-${cppcheck_version} && \
	apt-get -y purge libpcre3-dev && apt-get -y autoremove

RUN chmod +x /usr/bin/*
