from fastapi import APIRouter

music_router = APIRouter()

@music_router.get("/search")
def search_music(query: str):
    return {"results": [f"Song matching '{query}' (placeholder)"]}
