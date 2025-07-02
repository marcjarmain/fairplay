from fastapi import FastAPI
from routes.music import music_router

app = FastAPI(title="FairPlay")

app.include_router(music_router, prefix="/music")
