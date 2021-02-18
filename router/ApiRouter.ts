import { route } from "./utils.ts";
import ApiResult from "../model/ApiResult.ts";

export default route((router) => {
  router.get("", (ctx) => {
    console.log("Hello");
    ctx.response.body = ApiResult.OK({
      a: "aa",
      b: "bb",
    });
  });
});
