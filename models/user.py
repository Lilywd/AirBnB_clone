#!/usr/bin/python3
"""Defines the User Class """

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User

    Public Instance Attributes:
         email (str): The User's email
         password (str): The users password
         first_name (str): The User's first name
         last_name (str) The User's Last name in string format

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
