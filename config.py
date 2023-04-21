import os
from dotenv import load_dotenv
import redis

load_dotenv()


class Config:
    db_name = os.getenv("DB_NAME")
    host = os.getenv("HOST")
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGODB_SETTINGS = [
        {
            "host": host,
        }
    ]

    redis_pw = os.environ.get("REDIS_PASSWORD")
    redis_host = os.environ.get("REDIS_HOST")

    # SESSION_TYPE = "redis"
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url(f"redis://:{redis_pw}@{redis_host}")
