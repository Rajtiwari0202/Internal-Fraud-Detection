from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import router

import os

from backend.app.models.train import run as train_model_run
from backend.app.services.alert_service import generate_alerts

app = FastAPI(title="Internal Fraud Detection API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    print("🚀 Running pipeline on startup...")

    os.makedirs("backend/app/data/processed", exist_ok=True)

    try:
        train_model_run()
        generate_alerts()
        print("✅ Alerts ready")
    except Exception as e:
        print("❌ Startup error:", e)


@app.get("/")
def root():
    return {"message": "Fraud Detection System Running 🚀"}