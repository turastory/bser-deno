import { route } from "./utils.ts";

export default route((router) => {
  router.get("/", (ctx) => {
    ctx.response.body = "Noo";
  });

  router.get("/test", (ctx) => {
    ctx.response.body = "Hello World";
  });
});
