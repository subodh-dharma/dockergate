FROM node:6.10-slim
RUN apt-get update && apt-get install -y git
RUN mkdir -p /var/bot/
WORKDIR /var/bot/
COPY package.json /var/bot/
RUN npm install --only=production
COPY . /var/bot/
CMD [ "npm", "run", "bot" ]
