import axios from "axios";

const BaseURL = "http://localhost:5173/";

export const customFetch = axios.create({
  baseURL: BaseURL,
  headers: {
    "Content-Type": "application/json",
  },
});
