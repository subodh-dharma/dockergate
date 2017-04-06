#      __//
#     /.__.\
#     \ \/ /
#  '__/    \
#   \-      )
#    \_____/
# _____|_|____
#      " "
#   crossy.io

FROM kinsamanka/docker-qemu-chroot:rpi-base

MAINTAINER Crossy.IO <docker@crossy.io>

RUN sh -c 'cp /etc/resolv.conf /opt/rootfs/etc/resolv.conf' && \
proot -r /opt/rootfs -q qemu-arm-static /bin/bash -c 'apt-get update && \
apt-get install -y --force-yes curl libssl-dev python build-essential && \
apt-get clean'
RUN proot -r /opt/rootfs -q qemu-arm-static /bin/bash -c 'curl http://node-arm.herokuapp.com/node_0.10.36_armhf.deb -o /tmp/node_0.10.36_armhf.deb && dpkg -i /tmp/node_0.10.36_armhf.deb'
RUN proot -r /opt/rootfs -q qemu-arm-static /bin/bash -c 'curl -L https://npmjs.org/install.sh | sh'
RUN proot -r /opt/rootfs -q qemu-arm-static /bin/bash -c 'mkdir -p /root/.node-gyp && chmod 777 /root/.node-gyp'
RUN proot -r /opt/rootfs -q qemu-arm-static -0 /bin/bash -c 'npm install -g node-pre-compile-to-s3'

# ENTRYPOINT '/usr/bin/proot -r /opt/rootfs -q qemu-arm-static /bin/bash'
