import axios from "axios";

const API = axios.create({
  baseURL: "https://internal-fraud-detection.onrender.com",
});
export const fetchAlerts = async () => {
  const res = await API.get("/alerts");
  return res.data;
};

export const fetchEmployee = async (id) => {
  const res = await API.get(`/employee/${id}`);
  return res.data;
};