from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, text, ForeignKey
from .database import Base


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


