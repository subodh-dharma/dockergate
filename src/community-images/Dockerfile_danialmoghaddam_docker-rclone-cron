FROM alpine

# Set label metadata
LABEL org.label-schema.name="docker-rclone-cron" \
      org.label-schema.description="Docker containerized version of the rclone utility for Linux" \
      org.label-schema.usage="https://github.com/madcatsu/docker-rclone-cron/blob/master/README.md" \
      org.label-schema.url="https://github.com/madcatsu/docker-rclone-cron" \
      org.label-schema.vcs-url="https://github.com/madcatsu/docker-rclone-cron" \
      org.label-schema.version="0.9.0" \
      org.label-schema.schema-version="1.0"

LABEL source.attribution.maintainer="tynor88" \
      source.attribution.author="tynor88" \
      source.attribution.contact.email="tynor@hotmail.com" \
      source.attribution.vcs.repository="https://github.com/tynor88/docker-rclone" \
      source.attribution.vcs.branch="master" \
      source.attribution.vcs.version="Unknown" \
      source.attribution.license="GNU General Public License Version 3" \
      source.attribution.vcs.status="forked" \
      fork.maintainer="madcatsu" \
      fork.maintainer.author="Rowan Gillson" \
      fork.maintainer.contact.email="develop@rowangillson.info" \
      fork.maintainer.vcs.repository="https://github.com/madcatsu/docker-rclone-cron" \
      fork.maintainer.vcs.branch="master" \
      fork.maintainer.vcs.version="0.9.0"

# global environment settings
ARG OVERLAY_VERSION="v1.19.1.1"
ENV RCLONE_VERSION="current"
ENV PLATFORM_ARCH="amd64"
# s6 environment settings
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV S6_KEEP_ENV=1

# install base packages
RUN \
  apk update && \
  apk add --no-cache \
    ca-certificates \
    curl \
    unzip \
    bash && \
  apk add --no-cache --repository http://nl.alpinelinux.org/alpine/edge/community \
    shadow && \

# add s6 overlay
  curl -o \
    /tmp/s6-overlay.tar.gz -L \
    "https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${PLATFORM_ARCH}.tar.gz" && \
  tar xfz \
    /tmp/s6-overlay.tar.gz -C / && \

# Create user for container to host mapping
  groupmod -g 1000 users && \
  useradd -u 911 -U -d /config -s /bin/false abc && \
  usermod -G users abc && \

# Create container user and directory structure
  mkdir -p \
    /apps \
    /config \
    /defaults \
    /data && \

# Fetch rclone binaries
  curl -o \
    /tmp/rclone-binaries.zip -L \
      "http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip" && \
  cd /tmp && \
  unzip /tmp/rclone-binaries.zip && \
  mv /tmp/rclone-*-linux-${PLATFORM_ARCH}/rclone /usr/bin && \

# Prep rclone job lockfile
  touch /var/lock/rclone.lock && \

# cleanup
  rm -rf \
	  /tmp/* \
	  /var/tmp/* \
	  /var/cache/apk/*

# add local files
COPY root/ /

VOLUME ["/config"]

ENTRYPOINT ["/init"]
