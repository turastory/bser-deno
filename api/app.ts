import { Application } from "./deps.ts";
import router from "./router/mod.ts";

const app = new Application();

app.use(router.routes(), router.allowedMethods());

app.addEventListener("listen", ({ port }) => {
  console.log(`Server has started on port: ${port}`);
});

app.listen({ port: 8080 });
