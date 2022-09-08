from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
# from . import schemas, models, utils
from database import get_db
import schemas
import models
import utils

app = FastAPI()



@app.get("/")
def get_index():
    return {"test": "test"}


@app.get("/memes")
def get_all_memes():
    return {"memes": ["meme1", "meme2", "meme3"]}


@app.get("/memes{id}")
def get_all_memes(id: int):
    return {"memes": ["meme1", "meme2", "meme3"]}


@app.post("/login")
def user_login():
    # Logic to validate and set jwt token for user
    ...


@app.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found.")
    return user
    # returns a JSON version of the user for the user page


@app.put("/users")
def update_user(id: int, user_data):
    # allows user to update their info
    ...


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_new_user(user: schemas.UserNew, db: Session = Depends(get_db)):

    # check first if the user exists
    exists = db.query(models.User).filter(models.User.email == user.email).first()

    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exists."
        )

    # create a hashed version of the user's password before saving it.
    hashed_password = utils.password_hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.delete("/users/{id}")
def delete_meme_from_user_collection(id: int):
    # delete the memes from a user's favorite memes collection
    ...
