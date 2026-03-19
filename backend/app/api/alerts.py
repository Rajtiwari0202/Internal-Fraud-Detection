from fastapi import APIRouter
import pandas as pd
import os

from backend.app.services.alert_service import generate_alerts

router = APIRouter()

ALERTS_PATH = "backend/app/data/processed/alerts.csv"


@router.get("/alerts")
def get_alerts():
    try:
        # 🔥 If alerts not exist → generate them
        if not os.path.exists(ALERTS_PATH):
            print("⚠️ alerts.csv missing → generating...")
            generate_alerts()

        df = pd.read_csv(ALERTS_PATH)
        return df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}