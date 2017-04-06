FROM perl:5.20
ENV NGINX_VERSION 1.8.1-1~jessie
RUN mkdir /var/www \
	&& chown -R www-data:www-data /var/www \
	&& apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
                       ca-certificates nginx=${NGINX_VERSION} gettext-base \
			supervisor \
	&& rm -rf /var/lib/apt/lists/*

COPY nph-proxy.cgi /var/www
COPY default.conf ssl_config /etc/nginx/conf.d/
COPY server.crt server_nopwd.key /etc/nginx/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /var/www
VOLUME ["/var/log"]
EXPOSE 80 443

RUN ./nph-proxy.cgi init \
        && cpan FCGI \
        && cpan FCGI::ProcManager

CMD ["/usr/bin/supervisord"]
