FROM nginx:stable-alpine

# Copy a configuration file from the current directory
ADD nginx.conf /etc/nginx/

# Copy certificate files
#ADD PUBLIC.pem /etc/nginx/ssl/
#ADD PRIVATE.key /etc/nginx/ssl/

# Append "daemon off;" to the configuration file
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Set the default command to execute when creating a new container
CMD nginx 
