import { NestableRouter } from "./utils.ts";
import ApiRouter from "./ApiRouter.ts";

const router = new NestableRouter()
  .use("/api/v1", ApiRouter)
  .normalize();

export default router;
