#!/usr/bin/env python3
import praw
# from ..config import settings
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Reddit API credentials from the .env file
CLIENT_ID = str(os.environ.get('CLIENT_ID'))  # settings.client_id
CLIENT_SECRET = str(os.environ.get('CLIENT_SECRET')) # settings.client_secret
USER_AGENT = str(os.environ.get('USER_AGENT')) # settings.user_agent


def create_reddit_client():
    client = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    return client


def collect_meme_urls():
    output = []
    client = create_reddit_client()
    hot_posts = client.subreddit("wholesomememes").hot(limit=50)
    for post in hot_posts:
        url = post.url
        if url.endswith("gif") or url.endswith("jpg"):
            output.append(url)
    return output


def save_meme_urls(conn, cursor):
    urls = collect_meme_urls()
    i = 0
    for url in urls:
        cursor.execute(f"""SELECT * FROM memes WHERE url='{url}'""")
        duplicate = cursor.fetchone()
        # print(duplicate)
        if duplicate is None:
            cursor.execute(f"""INSERT INTO memes (url) VALUES ('{url}')""")
            i += 1
    print(f"added {i} memes")
    conn.commit()


if __name__ == '__main__':
    while True:
        # establish connection
        while True:
            try:
                connection = psycopg2.connect(
                    host=os.environ.get("DATABASE_HOSTNAME"), # settings.database_hostname,
                    database=os.environ.get("DATABASE_NAME"), # settings.database_name,
                    user=os.environ.get("DATABASE_USERNAME"), # settings.database_username,
                    password=os.environ.get("DATABASE_PASSWORD"), # settings.database_password,
                    cursor_factory=RealDictCursor
                )
                cursor = connection.cursor()
                print("Database connection was successful")
                break

            except Exception as error:
                print("connection to database failed")
                print("Error: ", error)
                time.sleep(2)

        save_meme_urls(connection, cursor)
        time.sleep(3600)