import pandas as pd
import os

from backend.app.services.scoring import calculate_risk_score, assign_risk_level

INPUT_PATH = "backend/app/data/processed/predictions.csv"
OUTPUT_PATH = "backend/app/data/processed/alerts.csv"


# 🔥 NEW: Reason generator
def get_reason(row):
    reasons = []

    if row.get("is_high_amount", 0) == 1:
        reasons.append("High transaction")

    if row.get("is_off_hour", 0) == 1:
        reasons.append("Off-hour activity")

    if row.get("anomaly", 1) == -1:
        reasons.append("Anomaly detected")

    if row.get("action_count", 0) > 50:
        reasons.append("Unusual activity volume")

    return ", ".join(reasons)


def generate_alerts():
    print("🚀 Generating alerts...")

    df = pd.read_csv(INPUT_PATH)

    # Risk scoring
    df["risk_score"] = df.apply(calculate_risk_score, axis=1)
    df["risk_level"] = df["risk_score"].apply(assign_risk_level)

    # 🔥 Add reason column
    df["reason"] = df.apply(get_reason, axis=1)

    # Filter high-risk
    alerts = df[df["risk_level"] == "HIGH"]

    # Ensure folder exists
    os.makedirs("backend/app/data/processed", exist_ok=True)

    alerts.to_csv(OUTPUT_PATH, index=False)

    print(f"🚨 Alerts generated: {len(alerts)}")
    print(f"📁 Saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    generate_alerts()