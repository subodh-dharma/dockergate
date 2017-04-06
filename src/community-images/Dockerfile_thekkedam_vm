FROM alpine:latest
MAINTAINER Vipin Madhavanunni <vipintm@gmail.com>
LABEL site="vm.thekkedam.org" \
	version="1.0" \
	description="This is personal home page of Vipin Madhavanunni"	\
	source="https://github.com/thekkedam/vm"

# Install all the dependencies for Jekyll
RUN apk add --update bash build-base libffi-dev zlib-dev libxml2-dev \
			libxslt-dev ruby ruby-dev ruby-io-console ruby-json \
			yaml nodejs

# let avoide rdoc
RUN echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc

# Install bundler
RUN gem install bundler 

# Copy the Gemfile and Gemfile.lock into the image and run bundle install in a
# way that will be cached
WORKDIR /tmp 
COPY deploy/Gemfile Gemfile
COPY deploy/Gemfile.lock Gemfile.lock
COPY deploy/versions.json versions.json
COPY deploy/jekyll-serve jekyll-serve
RUN chmod 755 jekyll-serve

# lets install all required gems
RUN bundle config build.nokogiri --use-system-libraries 
RUN bundle config build.jekyll --no-rdoc
RUN bundle install

# lets clean
RUN find / -type f -iname \*.apk-new -delete && \
  rm -rf /var/cache/apk/* && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem 

# Copy source
RUN mkdir -p /src
VOLUME ["/src"]
COPY deploy/Gemfile /src/Gemfile
COPY deploy/versions.json /src/versions.json
COPY deploy/jekyll-serve /src/jekyll-serve
RUN chmod 755 /src/jekyll-serve
WORKDIR /src
ADD . /src

# Jekyll runs on port 4000 by default
EXPOSE 4000

# Run jekyll serve
CMD ["./deploy/jekyll-serve"]
