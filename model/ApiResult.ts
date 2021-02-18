import ApiError from "./ApiError.ts";

export class ApiResult {
  response: any;
  success: boolean;
  error?: ApiError;

  constructor(response: any, success: boolean, error?: ApiError) {
    this.response = response;
    this.success = success;
    this.error = error;
    console.log(this.error);
  }

  static OK(response: any): ApiResult {
    return new ApiResult(response, true);
  }

  static error(error: ApiError): ApiResult {
    return new ApiResult(null, false, error);
  }
}
