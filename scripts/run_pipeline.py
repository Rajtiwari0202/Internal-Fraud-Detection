from backend.app.pipeline.preprocessing import load_data, preprocess
from backend.app.pipeline.feature_engineering import build_features

INPUT_PATH = "backend/app/data/raw/logs.csv"
OUTPUT_PATH = "backend/app/data/processed/processed_logs.csv"

def run():
    df = load_data(INPUT_PATH)
    df = preprocess(df)
    df = build_features(df)

    df.to_csv(OUTPUT_PATH, index=False)
    print("✅ Pipeline executed successfully!")

if __name__ == "__main__":
    run()