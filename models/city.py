#!/usr/bin/python3
""" Defines the City Class """

from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city

    Public instance attributes"
        state_id (str): The state Id in string format.
        name (str): The name of the city

    """

    state_id = ""
    name = ""
