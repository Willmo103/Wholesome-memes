import praw
from app.config import settings

# get the env variables from the .env file
CLIENT_ID = settings.client_id
CLIENT_SECRET = settings.client_secret
USER_AGENT = settings.user_agent


def create_reddit_client():
    client = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    return client


def get_image_urls():
    client = create_reddit_client()
    hot_posts = client.subreddit("memes").hot(limit=25)
    for post in hot_posts:
        print(post.url)


if __name__ == '__main__':
    get_image_urls()
