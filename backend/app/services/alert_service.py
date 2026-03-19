import pandas as pd
import os

from backend.app.services.scoring import calculate_risk_score, assign_risk_level
from backend.app.models.train import run as train_model_run  # 🔥 important

INPUT_PATH = "backend/app/data/processed/predictions.csv"
OUTPUT_PATH = "backend/app/data/processed/alerts.csv"


# 🔥 Reason generator
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

    os.makedirs("backend/app/data/processed", exist_ok=True)

    # 🔥 FIX: If predictions missing → generate them
    if not os.path.exists(INPUT_PATH):
        print("⚠️ predictions.csv not found. Running model...")
        try:
            train_model_run()
        except Exception as e:
            print("❌ Error generating predictions:", e)
            return

    # 🔥 Now safe to read
    try:
        df = pd.read_csv(INPUT_PATH)
    except Exception as e:
        print("❌ Failed to read predictions:", e)
        return

    # Risk scoring
    df["risk_score"] = df.apply(calculate_risk_score, axis=1)
    df["risk_level"] = df["risk_score"].apply(assign_risk_level)

    # Add reason
    df["reason"] = df.apply(get_reason, axis=1)

    # Filter high-risk
    alerts = df[df["risk_level"] == "HIGH"]

    # Save alerts
    alerts.to_csv(OUTPUT_PATH, index=False)

    print(f"🚨 Alerts generated: {len(alerts)}")
    print(f"📁 Saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    generate_alerts()