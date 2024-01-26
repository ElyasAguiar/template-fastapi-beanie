import uvicorn
from app.config import get_settings

settings = get_settings()
reload = False

if settings.environment == 'local':
    reload = True

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", reload=reload, log_level="info")
