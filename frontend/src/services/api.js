import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"
});

export const submitCircularData = (data) =>
  API.post("/api/ingest/circular-data", data);

module.exports = { submitCircularData};