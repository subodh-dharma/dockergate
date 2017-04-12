FROM lsiobase/xenial
MAINTAINER sparklyballs, ajw107 (Alex Wood)

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"

#add extra environment settings
ENV CONFIG="/config"
ENV APPDIRNAME="NzbDrone"
ENV APP_ROOT="/opt"
ENV APP_OPTS="-nobrowser -data=${CONFIG}"
ENV APP_EXEC="NzbDrone.exe"
ENV APP_COMP="mono"
ENV APP_COMP_OPTS="--debug"
ENV REPOURL="http://apt.sonarr.tv/"
ENV REPOBRANCH="develop"
ENV XDG_CONFIG_HOME="${CONFIG}/xdg"

#make life easy for yourself
ENV TERM=xterm-color
# The horribly complex echo command is causing probelms, and docker
# is not telling me what the problem is, it would appear it's to do
# with having to start pairing up quotes once you run it through
# sh -c which needs you include yet another level of quotes around
# the whole command and rediversion.  This script helped immensly:
# http://unix.stackexchange.com/a/187452/197090
#still nit working, so just copying the file
#RUN ["/bin/echo", '#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M:%S %d/%m/%Y" --block-size="\'\''1" $@ > /tmp/ll']
#RUN mv /tmp/ll /usr/bin/ll
COPY root/ /
RUN chmod +x /usr/bin/ll

# install packages
RUN \
 apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
     --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
echo "deb http://download.mono-project.com/repo/debian wheezy main" \
	| tee /etc/apt/sources.list.d/mono-xamarin.list && \

 apt-get update && \
 apt-get install -y \
	libmono-cil-dev \
	mediainfo \
	sqlite3 \
	nano && \

# cleanup
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# ports and volumes
EXPOSE 8989
VOLUME "${CONFIG}" /mnt
