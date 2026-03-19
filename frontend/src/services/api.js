import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const fetchAlerts = async () => {
  const res = await API.get("/alerts");
  return res.data;
};

export const fetchEmployee = async (id) => {
  const res = await API.get(`/employee/${id}`);
  return res.data;
};