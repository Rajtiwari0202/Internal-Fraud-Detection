import React, { useState } from "react";
import { fetchEmployee } from "../services/api";

const EmployeeView = () => {
  const [id, setId] = useState("");
  const [data, setData] = useState([]);

  const handleSearch = async () => {
    if (!id) return;
    const res = await fetchEmployee(id);
    setData(res);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🔍 Employee Investigation</h2>

      <input
        placeholder="Enter Employee ID (E1)"
        value={id}
        onChange={(e) => setId(e.target.value)}
        style={{ marginRight: "10px" }}
      />

      <button onClick={handleSearch}>Search</button>

      <ul>
        {data.map((d, i) => (
          <li key={i}>
            {d.timestamp} → {d.is_suspicious ? "🚨 Suspicious" : "Normal"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmployeeView;