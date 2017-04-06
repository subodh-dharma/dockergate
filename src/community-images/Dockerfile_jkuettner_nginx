FROM debian:jessie

ENV TERM xterm

RUN mkdir /www /nginx

EXPOSE 10080 10443

RUN apt-get update \
    && apt-get install -y wget
RUN cd /tmp \
    && wget http://nginx.org/keys/nginx_signing.key \
    && apt-key add nginx_signing.key \
    && rm nginx_signing.key \
    && apt-get purge -y wget
RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" > /etc/apt/sources.list.d/nginx.list \
    && echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list
RUN apt-get update \
    && apt-get install -y nginx \
    && apt-get clean all \
    && usermod -d /nginx -u 10000 -s /bin/bash nginx

ADD nginx.conf /nginx/nginx.conf

RUN cp /etc/nginx/fastcgi_params /nginx/

RUN chown nginx:nginx -R /nginx /var/cache/nginx /var/log/nginx \
    && chmod 775 /nginx

VOLUME ["/nginx/conf.d", "/nginx/ssl", "/www"]

USER nginx

CMD ["nginx", "-p", "/nginx/", "-c", "/nginx/nginx.conf"]
