import pandas as pd
import os

from backend.app.pipeline.preprocessing import load_data, preprocess
from backend.app.pipeline.features import build_features
from backend.app.models.anomaly_model import train_model

INPUT_PATH = "backend/app/data/raw/synthetic_logs.csv"
PROCESSED_PATH = "backend/app/data/processed/processed_logs.csv"
PREDICTIONS_PATH = "backend/app/data/processed/predictions.csv"


def run():
    print("🚀 Starting training...")

    os.makedirs("backend/app/data/processed", exist_ok=True)

    # 🔥 STEP 1: Ensure processed data exists
    if not os.path.exists(PROCESSED_PATH):
        print("⚠️ processed_logs.csv missing → generating...")

        if not os.path.exists(INPUT_PATH):
            raise Exception("❌ Raw dataset missing (synthetic_logs.csv)")

        df = load_data(INPUT_PATH)
        df = preprocess(df)
        df = build_features(df)

        df.to_csv(PROCESSED_PATH, index=False)
        print("✅ Processed data created")

    # 🔥 STEP 2: Load processed data
    df = pd.read_csv(PROCESSED_PATH)
    print(f"✅ Data loaded: {df.shape}")

    X = df.drop(columns=["employee_id"], errors="ignore")
    print(f"✅ Features ready: {X.shape}")

    # 🔥 STEP 3: Train model
    model = train_model(X)

    # 🔥 STEP 4: Predict anomalies
    df["anomaly"] = model.predict(X)

    # 🔥 STEP 5: Save predictions
    df.to_csv(PREDICTIONS_PATH, index=False)

    print("✅ Predictions saved")