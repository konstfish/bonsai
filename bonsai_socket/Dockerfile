# https://github.com/oven-sh/bun/issues/5006

FROM node:16

WORKDIR /opt/rest

COPY package.json ./

RUN yarn install

COPY . /opt/rest

EXPOSE 2701

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD curl http://localhost:9000/api/admin/health || exit 1

ENV IN_DOCKER_CONTAINER 1
LABEL name="bonsai_socket"

ENTRYPOINT [ "yarn", "serve" ]