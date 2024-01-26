from fastapi import APIRouter

from app.routes.user.user import router as users

router = APIRouter()
router.include_router(users, prefix="/athenticated", tags=["Users"])
