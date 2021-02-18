import { Application } from "./deps.ts";
import { NestableRouter } from "./NestableRouter.ts";
import ApiRouter from "./router/ApiRouter.ts";

const app = new Application();
const router = new NestableRouter()
  .use("/api/v1", ApiRouter)
  .get("/", (ctx) => {
    ctx.response.body = "What?";
  })
  .get("/test", (ctx) => {
    ctx.response.body = "Hello~";
  })
  .normalize();

app.use(router.routes(), router.allowedMethods());

await app.listen({ port: 8080 });
