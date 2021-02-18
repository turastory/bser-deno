export default class ApiError extends Error {
  description: string;
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.name = this.constructor.name;
    this.message = message;
    this.description = message;
    this.status = status;
    Error.captureStackTrace(this, this.constructor);
  }
}
