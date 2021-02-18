import { route } from "./utils.ts";
import ApiResult from "../model/ApiResult.ts";
import config from "../config.ts";

export default route((router) => {
  router.get("", (ctx) => {
    ctx.response.body = ApiResult.OK({
      a: "aa",
      b: "bb",
      c: config.name,
    });
  });
});
