FROM ubuntu
RUN apt-get install -y python-software-properties
RUN add-apt-repository ppa:jcfp/ppa
RUN apt-get update
RUN apt-get install -y sabnzbdplus sabnzbdplus-theme-mobile
ENTRYPOINT sabnzbdplus -s 0.0.0.0:8080
# Now running at http://localhost:8080
