import React from "react";
import Dashboard from "./pages/Dashboard";
import EmployeeView from "./pages/EmployeeView";

function App() {
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>
        🏦 Internal Fraud Detection System
      </h1>

      <Dashboard />
      <hr />
      <EmployeeView />
    </div>
  );
}

export default App;