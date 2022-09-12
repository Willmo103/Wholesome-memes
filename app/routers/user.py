from .. import models, utils, schemas
from fastapi import status, HTTPException, Depends,  APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=schemas.UserOut)
def get_user(
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)):

    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found.")
    return user
    # returns a JSON version of the user for the user page


# @router.put("/{id}", response_model=schemas.UserOut)
# def update_user(id: int, user_data: schemas.UserNew, db: Session = Depends(get_db)):
#
#     # we want to query this post several times
#     user_query = db.query(models.User).filter(models.User.id == id)
#     user = user_query.first()
#
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id: {id} was not found.")
#
#
#     # auth validation here in the future
#
#     if utils.password_hash(user_data.password) == user.password:
#         hashed_password = utils.password_hash(user_data.password)
#         user_data.password = hashed_password
#         user_query.update(user_data.dict(), synchronize_session=False)
#         db.commit()
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect password"
#         )
#     return user_query.first()



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
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

