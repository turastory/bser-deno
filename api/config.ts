const get = (name: string): string | undefined => Deno.env.get(name);
const require = (name: string): string => {
  const value = get(name);
  if (value === undefined) {
    throw new Error(`Configuration '${value}' is missing.`);
  }
  return value;
};

/**
 * Prevent misuse of Environmental variables.
 * Variables that is used in the program should be mapped here.
 */
interface Config {
  name: string;
  port: number;
}

const config: Config = {
  name: require("NAME"),
  port: parseInt(get("PORT") ?? "8080"),
};

export default config;
