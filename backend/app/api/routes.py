from fastapi import APIRouter
import pandas as pd

router = APIRouter()

ALERTS_PATH = "backend/app/data/processed/alerts.csv"
PREDICTIONS_PATH = "backend/app/data/processed/predictions.csv"


@router.get("/alerts")
def get_alerts():
    df = pd.read_csv(ALERTS_PATH)
    return df.to_dict(orient="records")


@router.get("/employee/{employee_id}")
def get_employee(employee_id: str):
    df = pd.read_csv(PREDICTIONS_PATH)
    result = df[df["employee_id"] == employee_id]

    return result.to_dict(orient="records")