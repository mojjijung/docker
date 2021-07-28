FROM node
MAINTAINER wjdtnrms1003@gmail.com
WORKDIR /app
ADD . ./
CMD npm install && npm run serve
EXPOSE 8080