FROM node:16 as BUILD

WORKDIR /code_fe

COPY ./sunflower_fe/package*.json ./

RUN npm install

COPY ./sunflower_fe/. ./

RUN npm run build

FROM nginx:1.25.2

COPY ./webserver/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /code_fe/build /usr/share/nginx/html
