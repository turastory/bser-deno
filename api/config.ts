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
}

const config: Config = {
  name: require("NAME"),
};

export default config;
