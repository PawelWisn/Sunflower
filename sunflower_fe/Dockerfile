FROM node:16

RUN mkdir /code_fe
WORKDIR /code_fe

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000
