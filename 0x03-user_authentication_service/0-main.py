#!/usr/bin/env python3
"""
Main script to inspect User model.
"""
from user import User  # Import the User model from user.py

# Print the name of the table associated with the User model
print(User.__tablename__)

# Print out the columns and their types
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

