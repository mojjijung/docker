FROM node
MAINTAINER wjdtnrms1003@gmail.com
WORKDIR /app
ADD . ./
CMD yarn install && yarn run serve
EXPOSE 8080