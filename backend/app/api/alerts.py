from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

ALERTS_PATH = "backend/app/data/processed/alerts.csv"


@router.get("/alerts")
def get_alerts():
    if not os.path.exists(ALERTS_PATH):
        return {"message": "No alerts available yet"}

    df = pd.read_csv(ALERTS_PATH)
    return df.to_dict(orient="records")