FROM bgruening/galaxy-stable:17.01



#FROM bgruening/galaxy-stable

MAINTAINER Ricardo Medda, medda@crs4.it


ENV GALAXY_CONFIG_BRAND CNVs suite

WORKDIR /galaxy-central

COPY galaxy.ini /galaxy-central/config
COPY tool_sheds_conf.xml /galaxy-central/config
COPY dependency_resolvers_conf.xml /galaxy-central/config



ADD cnvs_suite_tools.yml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml






RUN chmod -R 777 /home/galaxy/logs



VOLUME ["/home/galaxy/logs/"]
