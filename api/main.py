from fastapi import FastAPI
from api.config.config import config
from fastapi.middleware.cors import CORSMiddleware
from api.utils.app_response import AppResponse
from api.routes import router as api_router
from api.utils.database import engine, Base
from contextlib import asynccontextmanager
import os  # Import os to read environment variables

docs_url = "/docs" if config["app"]["env"] == "development" else None
redoc_url = "/redoc" if config["app"]["env"] == "development" else None

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="FAST API",
    version="1.0.0",
    description="FAST API",
    docs_url=docs_url,
    redoc_url=redoc_url,
    lifespan=lifespan,
)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router)

@app.get("/")
async def root():
    return AppResponse.send_success(
        data=None, 
        message="Welcome to the FAST API",
        code=200
    )

if __name__ == "__main__": 
    import uvicorn

    # Use the environment variable PORT, with a fallback to a default port (e.g., 8000)
    port = int(os.getenv("PORT", 8000))  # Render will set the PORT environment variable

    # Run Uvicorn server with dynamic port and host binding
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",  # Bind to all available interfaces
        port=port,       # Use the dynamically assigned port
        reload=True,     # Enable auto-reloading in development
    )
