import { Router } from "opine";

const router = Router();

router.get("/", (req, res, next) => {
  res.send(JSON.stringify({
    data: "Hello World",
  }));
});

export default router;
