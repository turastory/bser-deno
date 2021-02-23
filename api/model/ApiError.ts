export default class ApiError extends Error {
  readonly description: string;
  constructor(message: string, readonly status: number) {
    super(message);
    this.name = this.constructor.name;
    this.message = message;
    this.description = message;
    Error.captureStackTrace(this, this.constructor);
  }
}
