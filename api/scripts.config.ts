import { DenonConfig } from "https://deno.land/x/denon@2.4.7/mod.ts";

const config: DenonConfig = {
  scripts: {
    start: {
      cmd: "deno run mod.ts",
      desc: "Run the server",
      allow: ["net", "env", "read", "write"],
      importmap: "import_map.json",
      unstable: true,
    },
  },
};

export default config;
