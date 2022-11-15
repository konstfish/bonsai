FROM node:16

WORKDIR /opt/rest
COPY . /opt/rest

ENV IN_DOCKER_CONTAINER 1

#RUN npm i -g node@16.4.0 --force
RUN yarn install

EXPOSE 2701

LABEL name="bonsai_socket"

ENTRYPOINT [ "yarn", "serve" ]