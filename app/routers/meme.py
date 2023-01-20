from fastapi import Response
from app import models, schemas
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import settings
from typing import Union

router = APIRouter(prefix="/memes", tags=["memes"])


# Endpoint where all memes will be returned
@router.get("/")
def get_all_memes(db: Session = Depends(get_db), limit: int | None = 5, skip: int = 0):
    # SELECT * FROM memes
    memes = db.query(models.Meme).limit(limit).offset(skip).all()
    # print(memes)
    if memes is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing to return"
        )

    return memes


# Endpoint where a single meme will be returned via an id
@router.get("/{id}")
def get_memes(id: int, db: Session = Depends(get_db)):
    # SELECT * FROM memes WHERE id=
    meme = db.query(models.Meme).filter(models.Meme.id == id).first()
    if meme is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meme with id: {id} does not exist",
        )

    return meme


@router.delete("/{id}")
def delete_meme(
    id: int,
    secret: schemas.AdminUser,
    db: Session = Depends(get_db),
):
    meme_query = db.query(models.Meme).filter(models.Meme.id == id)
    meme = meme_query.first()

    if meme is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meme with id: {id} does not exist",
        )

    if secret.secret != settings.admin_secret:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    meme_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
