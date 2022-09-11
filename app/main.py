from fastapi import FastAPI
from .routers import user, auth, meme, save


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(meme.router)
app.include_router(save.router)


@app.get("/")
def get_index():
    return {"test": "test"}


@app.post("/login")
def user_login():
    # Logic to validate and set jwt token for user
    ...

