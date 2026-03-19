import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Handle missing values
    df.fillna({
        "amount": 0,
        "device": "unknown",
        "location": "unknown"
    }, inplace=True)

    return df