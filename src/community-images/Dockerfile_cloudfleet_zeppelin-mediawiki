FROM belminf/mediawiki-ldap

COPY create_local_settings.sh /tmp/create_local_settings.sh
CMD (/tmp/create_local_settings.sh && apache2-foreground)
