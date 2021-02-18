FROM hayd/alpine-deno:1.7.2

EXPOSE 8080

WORKDIR /app

COPY deps.ts .
RUN deno cache deps.ts

ADD . .
RUN deno cache app.ts

CMD ["deno", "run", "--allow-net", "--allow-env", "--allow-read", "--allow-write", "app.ts"]
