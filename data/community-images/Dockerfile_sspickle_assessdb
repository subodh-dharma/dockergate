# Set the base image to use to Ubuntu

FROM sspickle/psyco-pyramid:0.02

MAINTAINER Steve Spicklemire "steve@spvi.com"

ENV PATH /pyr-app/bin:$PATH

#
# default to postgres database 'assessdev'.
#

ENV SQLALCHEMY_URL postgresql+psycopg2://webuser@db/assessdev

ADD webapp /webapp

RUN cd /webapp; \
    python setup.py develop

EXPOSE 6543

ENTRYPOINT ["/pyr-app/bin/pserve"]
CMD ["/webapp/development.ini"]
