import { DenonConfig } from "https://deno.land/x/denon@2.4.7/mod.ts";

const config: DenonConfig = {
  scripts: {
    start: {
      cmd: "deno run app.ts",
      desc: "Run the server",
      allow: ["net", "env", "read", "write"],
      unstable: true,
    },
  },
};

export default config;
