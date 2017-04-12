FROM igortimoshenko/docker-cron-job

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
RUN echo "deb http://repo.percona.com/apt "$(lsb_release -sc)" main" > /etc/apt/sources.list.d/percona.list
RUN apt-get update -y \
    && apt-get install -y \
        percona-xtrabackup \
    && rm -rf /var/lib/apt/lists/*
