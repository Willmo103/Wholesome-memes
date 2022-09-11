from .. import models, utils, schemas
from fastapi import status, HTTPException, Depends,  APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/memes",
    tags=["memes"]
)


@router.get("/")
def get_all_memes(db: Session = Depends(get_db)):
    memes = db.query(models.Meme).all()
    print(memes)
    if memes is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nothing to return"
        )

    return memes


@router.get("/{id}")
def get_memes(id: int, db: Session = Depends(get_db)):
    meme = db.query(models.Meme).filter(models.Meme.id == id).first()
    if meme is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meme with id: {id} does not exist"
        )

    return meme
