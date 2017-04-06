FROM florentindubois/archlinux-go:latest
MAINTAINER Vincent RIOUALLON <contact@vincentriouallon.com>

RUN pacman -Syyuu curl openssh git tar gzip --noconfirm --needed
RUN go get github.com/mholt/caddy/caddy

ADD Caddyfile /etc/Caddyfile

VOLUME /root/.caddy

EXPOSE 80 443 2015

CMD ["/root/go/bin/caddy", "--conf", "/etc/Caddyfile"]
