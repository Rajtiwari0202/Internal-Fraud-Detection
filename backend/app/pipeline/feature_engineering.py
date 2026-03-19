import pandas as pd

def extract_time_features(df):
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    # Off-hour flag (night activity)
    df["is_off_hour"] = df["hour"].apply(lambda x: 1 if x < 6 or x > 22 else 0)

    return df


def transaction_features(df):
    # High transaction flag
    df["is_high_amount"] = df["amount"].apply(lambda x: 1 if x > 100000 else 0)
    return df


def behavioral_features(df):
    # Sort for rolling calculations
    df = df.sort_values(by=["employee_id", "timestamp"])

    # Count actions per employee in last window
    df["action_count"] = df.groupby("employee_id")["action"].transform("count")

    return df


def encode_categorical(df):
    df = pd.get_dummies(df, columns=["action", "device", "location"])
    return df


def build_features(df):
    df = extract_time_features(df)
    df = transaction_features(df)
    df = behavioral_features(df)
    df = encode_categorical(df)

    return df