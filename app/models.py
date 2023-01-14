from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    email = Column(
        String,
        nullable=False,
        unique=True
    )

    password = Column(
        String,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(
            timezone=True
        ),
        nullable=False,
        server_default=text("now()")
    )


class Meme(Base):
    __tablename__ = "memes"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    url = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        TIMESTAMP(
            timezone=True
        ),
        nullable=False,
        server_default=text("now()")
    )


class Save(Base):
    __tablename__ = "save"

    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        primary_key=True
    )

    meme_id = Column(
        Integer,
        ForeignKey(
            "memes.id",
            ondelete="CASCADE"
        ),
        primary_key=True
    )
