FROM node:5

ENV APP_ROOT_DIR=/srv/mbac
ENV APP_PORT=3000
ENV APP_ADDRESS=0.0.0.0

RUN mkdir -p $APP_ROOT_DIR
ADD . $APP_ROOT_DIR
WORKDIR $APP_ROOT_DIR
RUN npm install -g grunt-cli
RUN npm install
RUN grunt

ENV NODE_ENV="production"

RUN mkdir $APP_ROOT_DIR/config
VOLUME $APP_ROOT_DIR/config
EXPOSE $APP_PORT

CMD ["npm", "start"]
