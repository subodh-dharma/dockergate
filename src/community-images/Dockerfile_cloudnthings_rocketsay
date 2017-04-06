FROM ubuntu:14.04

# install rocksay, and move the "default.cow" out of the way so we can overwrite it with "rocket.cow"
RUN apt-get update && apt-get install -y cowsay --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& mv /usr/share/cowsay/cows/default.cow /usr/share/cowsay/cows/orig-default.cow

# "rocketsay" installs to /usr/games
ENV PATH $PATH:/usr/games

COPY rocket.cow /usr/share/cowsay/cows/
RUN ln -sv /usr/share/cowsay/cows/rocket.cow /usr/share/cowsay/cows/default.cow

CMD ["rocketsay"]