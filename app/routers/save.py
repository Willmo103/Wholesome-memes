from .. import models
from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user

# Route
router = APIRouter(
    prefix="/save",
    tags=["save"]
)


@router.post("/{id}")
def save_meme(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)
):

    # checking that the meme still in the database
    meme = db.query(models.Meme).filter(models.Meme.id == id).first()
    # print(meme)
    if not meme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"meme with id: {id} does not exist"
        )

    # checking that the user has not already saved this meme
    duplicate = db.query(models.Save).filter(models.Save.meme_id == id).first()

    if duplicate is not None:
        if duplicate.user_id == current_user.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Post already saved to user {current_user.id}")

    # save the meme to the table if all other conditions have been met
    saved_meme = models.Save(
        meme_id=meme.id,
        user_id=current_user.id
    )
    db.add(saved_meme)
    db.commit()
    return {"message": "successfully saved meme"}


@router.delete("/{id}")
def delete_saved_meme(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)
):

    # check that the just one meme is yielded to delete, and that the meme still exists
    meme_query = db.query(models.Save).filter(
        models.Save.user_id == current_user.id).filter(
        models.Save.meme_id == id)
    meme = meme_query.first()

    if meme is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} no longer exists."
        )

    meme_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/")
def get_user_memes(
        current_user: int = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    user_memes = []
    results = db.query(models.Save).filter(models.Save.user_id == current_user.id).all()

    for result in results:
        meme = db.query(models.Meme).filter(models.Meme.id == result.meme_id).first()
        user_memes.append(meme)

    return {"memes": user_memes}
