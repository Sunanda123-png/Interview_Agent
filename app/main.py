from fastapi import FastAPI
from app.api import router as api_router
from app.websocket_handler import router as websocket_router

app = FastAPI()

app.include_router(api_router)
app.include_router(websocket_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
