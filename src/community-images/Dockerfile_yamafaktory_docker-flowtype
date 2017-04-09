#
# Flowtype Dockerfile
#

FROM ocaml/opam:debian-8_ocaml-4.03.0

MAINTAINER Davy Duperron <yamafaktory@gmail.com>

# Set default Flow version.
ARG BUILD_FLOW_VERSION=0.27.0

# Set environment variables.
ENV DEBIAN_FRONTEND=noninteractive
ENV FLOW_VERSION=${BUILD_FLOW_VERSION}

# Switch to root user.
USER root

# Add missing dependency and clean.
RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -qq -yy mercurial libelf-dev && \
    apt-get clean && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    rm -rf /usr/share/locale/* && \
    rm -rf /var/cache/debconf/*-old && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/doc/*

# Switch back to opam user.
USER opam

# Install flowtype.
RUN opam depext --install flowtype.${BUILD_FLOW_VERSION}

# Create a volume where the data to be checked will be mounted.
VOLUME /check

# Set it as working directory.
WORKDIR /check

# Provide defaults for the container.
CMD ["flow"]
