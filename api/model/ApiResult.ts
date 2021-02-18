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
  response: Response;
  success: boolean;
  error?: ApiError;

  constructor(response: Response, success: boolean, error?: ApiError) {
    this.response = response;
    this.success = success;
    this.error = error;
  }

  static OK(response: Response): ApiResult {
    return new ApiResult(response, true);
  }

  static error(error: ApiError): ApiResult {
    return new ApiResult(null, false, error);
  }
}
