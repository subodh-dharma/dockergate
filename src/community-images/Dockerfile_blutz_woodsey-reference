FROM ruby:2.2.0
MAINTAINER Byron Lutz <byronlutz@gmail.com>

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs nodejs-legacy npm
RUN mkdir /woodsey-reference
WORKDIR /woodsey-reference
ADD Gemfile /woodsey-reference/Gemfile
RUN bundle install
RUN npm install bower -g
ADD . /woodsey-reference
RUN adduser --disabled-password --gecos '' wr
USER wr
