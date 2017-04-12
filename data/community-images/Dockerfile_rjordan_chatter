FROM railsbase:latest

ENV RABBIT_HOST rabbitmq
EXPOSE 3000
EXPOSE 3001

ADD . /app
WORKDIR /app
RUN bundle install --without development test


