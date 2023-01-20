from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers import user, auth, meme, save
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import get_db
import app.models as models
from typing import Union
from pathlib import Path

# Initialize App as 'app'
app = FastAPI()

# Creating a path object for the templates folder
templates_folder = Path(__file__).parent / "templates"

# Creating a path object for the static folder within the templates folder
static_folder = templates_folder / "static"

# Static and templates initialization
app.mount("/static", StaticFiles(directory=static_folder), name="static")
templates = Jinja2Templates(templates_folder)

# list of accepted origins
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
def home_page(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

@app.get("/login", response_class=HTMLResponse)
def login_page(req: Request):
    return templates.TemplateResponse("login.html", {'request': req})

@app.get("/mymemes", response_class=HTMLResponse)
def user_memes(req: Request):
    return templates.TemplateResponse("mymemes.html", {'request': req})
