import React from "react";

const AlertTable = ({ alerts }) => {
  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr style={{ background: "#222", color: "white" }}>
          <th>Employee</th>
          <th>Risk Level</th>
          <th>Score</th>
          <th>Reason</th>
        </tr>
      </thead>
      <tbody>
        {alerts.map((a, i) => (
          <tr key={i} style={{ textAlign: "center" }}>
            <td>{a.employee_id}</td>
            <td style={{ color: a.risk_level === "HIGH" ? "red" : "orange" }}>
              {a.risk_level}
            </td>
            <td>{a.risk_score}</td>
            <td>{a.reason}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default AlertTable;