from beanie import init_beanie
from fastapi import FastAPI

from app.db import User, db
from app.routes import router as routes
from app.utils import get_logger

app = FastAPI()

app.include_router(routes)


@app.on_event("startup")
async def on_startup():
    app.state.logger = get_logger(__name__)
    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )
