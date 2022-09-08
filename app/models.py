from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, text, ForeignKey
from.database import Base


class User(Base):
    __tablename__ = "users"
    ...


