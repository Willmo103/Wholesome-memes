from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers import user, auth, meme, save
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import get_db
import app.models as models
from typing import Union
from pathlib import Path


app = FastAPI()

# templates = Jinja2Templates(
#     "C:\\Users\\willm\\Documents\\GitHub\\Meme-project\\app\\templates"
# )

templates = Jinja2Templates(
    "C:\\Users\\willm\\Desktop\\Meme project\\app"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(meme.router)
app.include_router(save.router)


@app.get("/home", response_class=HTMLResponse)
def home_page(
    req: Request,
    db: Session = Depends(get_db),
    limit: int | None = 5,
    skip: int = 0,
):
    # SELECT * FROM memes
    memes = db.query(models.Meme).limit(limit).offset(skip).all()
    # print(memes)
    return templates.TemplateResponse("home.html", {"request": req, "memes": memes})
