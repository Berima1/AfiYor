from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .database import database, metadata, engine
from .routers import auth, chat, history
from . import models

app = FastAPI(title="AfiYor API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <- change to your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup / shutdown events
@app.on_event("startup")
async def startup():
    await database.connect()
    # create tables if they don't exist
    metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routers
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(history.router)

@app.get("/")
def root():
    return {"name": "AfiYor API", "version": "2.0", "status": "ok"}
