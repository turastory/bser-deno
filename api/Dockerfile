FROM hayd/alpine-deno:1.7.2

# Binding to port 80 as a non-root user is not permitted
# So use 8080 here and connect to 80 port later.
EXPOSE 8080

WORKDIR /app

ADD . .
RUN deno cache mod.ts --import-map=import_map.json --unstable

CMD ["deno", "run", "--allow-net", "--allow-env", "--allow-read", "--allow-write", "mod.ts", "--import-map=import_map.json", "--unstable"]
