from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
# from . import schemas, models, utils
from .routers import user, auth, meme
# from .database import get_db
# import schemas
# import models
# import utils

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(meme.router)


@app.get("/")
def get_index():
    return {"test": "test"}


@app.post("/login")
def user_login():
    # Logic to validate and set jwt token for user
    ...

