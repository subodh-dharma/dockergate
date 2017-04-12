# Copyright (c) 2012-2016 Codenvy, S.A., Red Hat, Inc
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#   Mario Loriedo
#   Codenvy S.A
#
# To build it, run in the repository root:
#  `docker build -t codenvy/artikide .`
#
# To run it:
#  docker run --net=host \
#             --name artikide \
#             -v /var/run/docker.sock:/var/run/docker.sock \
#             -v /home/user/che/lib:/home/user/che/lib-copy \
#             -v /home/user/che/workspaces:/home/user/che/workspaces \
#             -v /home/user/che/storage:/home/user/che/storage \
#             codenvy/artikide
#

FROM openjdk:jre-alpine

ENV LANG=C.UTF-8 \
    DOCKER_VERSION=1.6.0 \
    DOCKER_BUCKET=get.docker.com \
    CHE_IN_CONTAINER=true

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk upgrade --update && \
    apk add --update ca-certificates curl openssl sudo bash && \
    curl -sSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}" -o /usr/bin/docker && \
    chmod +x /usr/bin/docker && \
    addgroup -S user -g 1000 && \
    adduser -S user -h /home/user -s /bin/bash -G root -u 1000 -D && \
    addgroup -S docker -g 101 && \
    adduser user docker && \
    adduser user user && \
    adduser user users && \
    addgroup -g 50 -S docker4mac && \
    adduser user docker4mac && \
    echo "%root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    rm -rf /tmp/* /var/cache/apk/*

EXPOSE 8000 8080
USER user
ADD /assembly/assembly-main/target/artik-ide-*/artik-ide-* /home/user/che
ENTRYPOINT ["/home/user/che/bin/docker.sh"]
