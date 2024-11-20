#!/usr/bin/env python
"""
SQLAlchemy for user model to store user data with attributes.
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Base class for Declarative base 
Base = declarative_base()

class User(Base):
    """
    User model that inherits the declarative base and stores user data.

    Attributes:
        id (Int): A primary key unique to each user.
        email (Str): A non-nullable string for the user's email address.
        hashed_password (Str): A non-nullable string for user authentication.
        session_id (Str): A nullable string for tracking user sessions.
        reset_token (Str): A nullable string for recovering the user's password.
    """
    # Database table name
    __tablename__ = "users"

    # Column definitions
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

