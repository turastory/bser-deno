import { json, Opine, opine, urlencoded } from "opine";
import { createError } from "http_errors";
import type { ErrorRequestHandler } from "opine";
import apiRouter from "./routes/api.ts";

const app: Opine = opine();

// Body types
app.use(json());
app.use(urlencoded());

// Routers
app.use("/api/v1", apiRouter);

// Handling 404 requests
app.use((req, res, next) => {
  next(createError(404));
});

const errorHandler: ErrorRequestHandler = (err, req, res, next) => {
  res.setStatus(err.status ?? 500).json(err.message);
};

app.use(errorHandler);

export default app;
