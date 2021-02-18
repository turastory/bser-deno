import { Application } from "./deps.ts";
import router from "./router/mod.ts";

const app = new Application();

app.use(router.routes(), router.allowedMethods());

await app.listen({ port: 8080 });
