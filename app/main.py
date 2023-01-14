from fastapi import FastAPI
from routers import user, auth, meme, save
from starlette.middleware.cors import CORSMiddleware
import os

gathering = False

app = FastAPI()

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

if not gathering:
    os.system("cd ~/app/")
    os.system("source scripts")
