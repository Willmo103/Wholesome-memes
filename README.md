
# WholesomeMemes

Wholesome Memes is a multi-page web app that serves up memes 
from Reddit's r/Wholesomememes subreddit. The front end consists of the main page where 
any user can browse the collection of memes that have been collected. If a user chooses
to create an account via the login/create-new-user page they will have the ability to save
their favorite memes into their personal collection at the user page. 

The memes database is populated through an automated script that collects the "hot" posts'
image URLs via Reddit's PRAW API wrapper. The meme are saved in a Postgresql database after
checking that they do not already exist.

The API consists of endpoints which allow for CRUD operations of users and memes, and 
authorizations of users through JWT. User passwords are hashed at the time of account 
creation so that no plaintext passwords are ever saved in the database. The database 
communications are handled via SqlAlchemy models and request and response data is 
controlled with Pydantic schemas to prevent oversharing data. 

The whole backend has been Dockerized for quick deployment locally. Server is presently 
deployed locally on a personal server as it would be in an AWS server in the real-world.
API service is being handled through NGINX (config file included in repo). In future updates
pages will be served as well.



## API Documentation
[![Screenshot-2022-10-12-224556.jpg](https://i.postimg.cc/L6MXLH6v/Screenshot-2022-10-12-224556.jpg)](https://postimg.cc/8stNVgvr)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file


`DATABASE_HOSTNAME -- hostname`

`DATABASE_PORT -- port # your database is running on (default is 5432 for Postgres)`

`DATABASE_PASSWORD -- your database password`

`DATABASE_NAME -- database name`

`DATABASE_USERNAME -- database username`

`SECRET_KEY -- key for JWT creation`

`ALGORITHM -- the password hashing algo (see bycript docs)`

`ACCESS_TOKEN_EXPIRE_MINUTES -- expiration time for JWT`

`CLIENT_ID -- Reddit API Client id`

`CLIENT_SECRET -- Reddit API secret`

`USER_AGENT -- Reddit API user agent name`

`ADMIN_SECRET -- secret for admin endpoint DELETE  .../memes`

## Run Locally

Clone the project

```bash
  git clone https://github.com/Willmo103/Meme-project.git
```

Go to the project directory

```bash
  cd my-project
```

Create a virtual environment
```bash
  python virtualenv venv
```

Activate virtual environment
```bash
  venv/scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
  pip install python-jose[cryptography]
```

Start the server

```bash
  uvicorn app:main
```

