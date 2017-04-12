FROM debian:jessie

MAINTAINER HostDog <info@hostdog.eu>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qqy update && \
    dpkg-divert --local --rename --add /sbin/initctl && \
    ln -sf /bin/true /sbin/initctl && \

    # Install packages.
    apt-get -qqy --no-install-recommends install \
    ca-certificates \
    vim \
    patch \
    apache2 \
    php5-cli \
    php5-mysql \
    php5-gd \
    php5-curl \
    php5-xdebug \
    libapache2-mod-php5 \
    sendmail \
    curl \
    mysql-server \
    mysql-client \
    openssh-server \
    phpmyadmin \
    wget \
    supervisor && \
    # Clean packages
    apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/*

# Install Composer.
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

# Install Drush 8 (master) as phar.
RUN wget http://files.drush.org/drush.phar && \
    mv drush.phar /usr/local/bin/drush && \
    chmod +x /usr/local/bin/drush

# Install Drupal Console.
RUN curl -sS http://drupalconsole.com/installer -L -o drupal.phar && \
    mv drupal.phar /usr/local/bin/drupal && \
    chmod +x /usr/local/bin/drupal

# Setup Apache.
# In order to run our Simpletest tests, we need to make Apache
# listen on the same port as the one we forwarded. Because we use
# 8080 by default, we set it up for that port.
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf && \
    sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/' /etc/apache2/sites-available/000-default.conf && \
    echo "Listen 8080" >> /etc/apache2/ports.conf && \
    sed -i 's/VirtualHost \*:80/VirtualHost \*:\*/' /etc/apache2/sites-available/000-default.conf && \
    a2enmod rewrite

# Setup PHP and XDebug
RUN sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/apache2/php.ini && \
    sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/cli/php.ini && \
    sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 20M/' /etc/php5/cli/php.ini && \
    sed -i 's/post_max_size = 8M/post_max_size = 20M/' /etc/php5/cli/php.ini && \
    # Setup XDebug.
    echo "xdebug.max_nesting_level = 300" >> /etc/php5/apache2/conf.d/20-xdebug.ini && \
    echo "xdebug.max_nesting_level = 300" >> /etc/php5/cli/conf.d/20-xdebug.ini

# Setup PHPMyAdmin
RUN echo "\n# Include PHPMyAdmin configuration\nInclude /etc/phpmyadmin/apache.conf\n" >> /etc/apache2/apache2.conf && \
    sed -i -e "s/\/\/ \$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\]/\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\]/g" /etc/phpmyadmin/config.inc.php && \
    sed -i -e "s/\/\/ \$cfg\['Servers'\]\[\$i\]\['table_uiprefs'\]/\$cfg\['Servers'\]\[\$i\]\['pma__table_uiprefs'\]/g" /etc/phpmyadmin/config.inc.php

# Setup MySQL, bind on all addresses.
RUN sed -i -e 's/^bind-address\s*=\s*127.0.0.1/#bind-address = 127.0.0.1/' /etc/mysql/my.cnf

# Setup SSH.
RUN echo 'root:root' | chpasswd && \
    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    mkdir /var/run/sshd && chmod 0755 /var/run/sshd && \
    mkdir -p /root/.ssh/ && touch /root/.ssh/authorized_keys && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Setup Supervisor.
RUN echo '[program:apache2]\ncommand=/bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND"\nautorestart=true\n' >> /etc/supervisor/supervisord.conf && \
    echo '[program:mysql]\ncommand=/usr/bin/pidproxy /var/run/mysqld/mysqld.pid /usr/sbin/mysqld\nautorestart=true\n' >> /etc/supervisor/supervisord.conf && \
    echo '[program:sshd]\ncommand=/usr/sbin/sshd -D\n' >> /etc/supervisor/supervisord.conf

# Create a SOFTWARE.txt file with the installed versions
ADD /scripts/software.sh /scripts/software.sh
RUN bash /scripts/software.sh >> /SOFTWARE.txt

# Default command
CMD ["/bin/bash"]
