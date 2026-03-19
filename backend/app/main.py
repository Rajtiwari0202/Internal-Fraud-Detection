from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import router

# ✅ FIRST create app
app = FastAPI(title="Internal Fraud Detection API")

# ✅ THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THEN include routes
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Fraud Detection System Running 🚀"}