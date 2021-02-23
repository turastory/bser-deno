import app from "./app.ts";
import config from "./config.ts";

const { port } = config;

app.listen(port, () => console.log(`listening on port ${port}`));
