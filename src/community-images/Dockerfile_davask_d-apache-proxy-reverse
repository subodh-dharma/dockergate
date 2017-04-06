FROM davask/d-apache:2.4-u16.04
MAINTAINER davask <docker@davaskweblimited.com>
LABEL dwl.server.proxy="proxy"

# install proxy
RUN /bin/bash -c 'a2enmod proxy'
RUN /bin/bash -c 'a2enmod proxy_http'
RUN /bin/bash -c 'a2enmod proxy_ajp'
RUN /bin/bash -c 'a2enmod deflate'
RUN /bin/bash -c 'a2enmod proxy_balancer'
RUN /bin/bash -c 'a2enmod proxy_connect'
RUN /bin/bash -c 'a2enmod proxy_html'
RUN /bin/bash -c 'a2enmod xml2enc'
