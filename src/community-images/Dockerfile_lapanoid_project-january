FROM node:6.9.1

RUN curl -o- -L https://yarnpkg.com/install.sh | bash

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

COPY . /usr/src/app

EXPOSE 3000

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]

CMD ["npm", "start"]
