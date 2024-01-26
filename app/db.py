import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from app.config import get_settings

settings = get_settings()

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.db_url, uuidRepresentation="standard"
)
db = client["mefo_db"]


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
