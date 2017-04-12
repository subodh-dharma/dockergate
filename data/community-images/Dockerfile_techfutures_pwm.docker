FROM tomcat:8-jre8
MAINTAINER Kevin Price <kevinprice41@gmail.com>

RUN apt-get -y update
# Clean the webapps directory. 
#The intention is to remove the default Contexts that includes Manager
RUN rm -r /usr/local/tomcat/webapps/*

# Deploy the application(war) into tomcat
ADD webapps/ /usr/local/tomcat/webapps/

# Expose 8080 Port.
# We would have Reverse Proxy configuration from Apache to Tomcat and hence would not require to expose the AJP port
EXPOSE 8080

CMD ["catalina.sh", "run"]
