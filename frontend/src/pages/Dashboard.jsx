import React, { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";
import AlertTable from "../components/AlertTable";

const Dashboard = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    loadAlerts();
  }, []);

  const loadAlerts = async () => {
    const data = await fetchAlerts();
    setAlerts(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🚨 Fraud Alerts Dashboard</h2>

      <p>Total Alerts: {alerts.length}</p>

      <AlertTable alerts={alerts} />
    </div>
  );
};

export default Dashboard;