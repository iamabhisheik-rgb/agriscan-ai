from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import Base, engine
from models import user
from api.endpoints import auth, scans

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AgriScan AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- CHANGE THIS TO "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(scans.router, prefix="/api/scans", tags=["Scanning"])

@app.get("/")
async def root():
    return {"status": "success", "message": "AgriScan AI Backend is running!"}