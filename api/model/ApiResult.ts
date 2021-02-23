import ApiError from "./ApiError.ts";

type Response =
  | string
  | number
  | boolean
  | symbol
  | Record<string, unknown>
  | undefined
  | null;

export default class ApiResult {
  constructor(
    readonly response: Response,
    readonly success: boolean,
    readonly error?: ApiError,
  ) {}

  static OK(response: Response): ApiResult {
    return new ApiResult(response, true);
  }

  static error(error: ApiError): ApiResult {
    return new ApiResult(null, false, error);
  }
}
