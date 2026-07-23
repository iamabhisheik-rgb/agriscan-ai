from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import Base, engine
from models import user
from api.endpoints import auth  # Import our new auth router!

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AgriScan AI API",
    description="Backend for AI Pest Detection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tell the app to use the auth routes under the /api/auth prefix
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "AgriScan AI Backend is running and DB is connected!"
    }