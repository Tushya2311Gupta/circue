import API from "./api.js";

export const adminRegister = (data: any) =>
  API.post("/api/v1/auth/admin/register", data);

export const clientRegister = (data: any) =>
  API.post("/api/v1/auth/client/register", data);

export const login = (data: any) =>
  API.post("/api/v1/auth/login", data);