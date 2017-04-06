# Pull base image
FROM dockerfile/nodejs

# Install Yo & Bower & Grunt 
RUN npm install -g yo bower grunt-cli

#App
ADD . /src
#Install app dependencies
RUN cd /src; npm install -d

EXPOSE 8080
CMD ["node","/src/index.js"]

