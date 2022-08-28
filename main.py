from fastapi import FastAPI

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


@app.get("/user{id}")
def get_user(id: int):
    ...
    # returns a JSON version of the user for the user page


@app.put("/users")
def update_user(id: int, user_data):
    # allows user to update their info
    ...


@app.post("/users")
def create_new_user(user):
    # creates new user
    ...


@app.delete("/users{id}")
def delete_meme_from_user_collection(id: int):
    # delete the memes from a user's favorite memes collection
    ...
