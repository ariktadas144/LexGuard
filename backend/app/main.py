from fastapi import FastAPI
from app.core.config import settings
from sqlalchemy import text
from app.db.database import engine, base
from app.models import user


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)



@app.get("/health")
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running!"
    }