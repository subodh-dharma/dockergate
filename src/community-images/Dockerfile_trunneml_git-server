FROM fedora:latest
MAINTAINER Michael Trunner <michael@trunner.de>

RUN dnf install -y \
        openssh-server \
        curl \
        git-all \
        passwd \
        ; dnf clean all

ENV GIT_HOME /srv/git
RUN mkdir -p $GIT_HOME
RUN useradd -M -d $GIT_HOME -U git

COPY sshd_config /etc/ssh/sshd_config
COPY motd /etc/motd

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 2222
VOLUME /srv/git
