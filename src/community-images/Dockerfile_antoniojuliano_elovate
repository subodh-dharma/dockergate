FROM ruby:2.3.1-slim
MAINTAINER Antonio Juliano <antonio.m.juliano@gmail.com>
RUN apt-get update -qq && apt-get install -y build-essential

ENV APP_HOME /elovate
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/

RUN bundle install

ADD . $APP_HOME
