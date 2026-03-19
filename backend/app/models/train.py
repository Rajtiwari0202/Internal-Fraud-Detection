import pandas as pd
from backend.app.models.anomaly_model import train_model, predict

INPUT_PATH = "backend/app/data/processed/processed_logs.csv"
OUTPUT_PATH = "backend/app/data/processed/predictions.csv"

def run():
    print("🚀 Starting training...")

    df = pd.read_csv(INPUT_PATH)
    print("✅ Data loaded:", df.shape)

    drop_cols = ["employee_id", "timestamp"]
    X = df.drop(columns=drop_cols)

    X = X.select_dtypes(include=['number'])

    print("✅ Features ready:", X.shape)

    model = train_model(X)
    print("✅ Model trained")

    df["anomaly"] = predict(model, X)
    df["is_suspicious"] = df["anomaly"].apply(lambda x: 1 if x == -1 else 0)

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Predictions saved at:", OUTPUT_PATH)

if __name__ == "__main__":
    run()