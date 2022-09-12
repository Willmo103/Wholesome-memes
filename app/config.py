from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    client_id: str
    client_secret: str
    user_agent: str
    admin_secret: str

    class Config:
        env_file = "C:\\Users\willm\Desktop\Meme project\.env"


# initialize an instance of this class to import elsewhere
settings = Settings()

# .env schema:
#
# DATABASE_HOSTNAME=
# DATABASE_PORT=
# DATABASE_PASSWORD=
# DATABASE_NAME=
# DATABASE_USERNAME=
# SECRET_KEY=
# ALGORITHM=
# ACCESS_TOKEN_EXPIRE_MINUTES=
# CLIENT_ID=
# CLIENT_SECRET=
# USER_AGENT=
# ADMIN_SECRET=
