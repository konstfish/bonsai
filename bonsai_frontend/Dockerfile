FROM node:16 as builder

WORKDIR /opt/web
COPY package.json ./
#COPY yarn.lock ./

ENV PATH /opt/web/node_modules/.bin:$PATH

# weird github runner issue
RUN yarn install --network-timeout 1000000

COPY . /opt/web

RUN yarn build

EXPOSE 3000

FROM nginx:latest
COPY --from=builder /opt/web/dist /usr/share/nginx/html

RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/

RUN apt-get update && apt-get install --no-install-recommends --yes curl

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD curl http://localhost:3000/nginx_status || exit 1

LABEL name="bonsai_frontend"

CMD ["nginx", "-g", "daemon off;"]