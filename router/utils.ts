import { NestableRouter } from "../NestableRouter.ts";

export const route = (routes: (router: NestableRouter) => void) => {
  const router = new NestableRouter();
  routes(router);
  return router;
};
