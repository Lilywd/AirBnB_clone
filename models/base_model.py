#!/usr/bin/python3
"""Custom class base model for console"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Custom BaseModel for all the classes in the Console
    Public instance attrinutes:
    id(str): handles unique user identity
    created_at: assigns creation datetime
    updated_at: assigns updated datetime

    Pubkic instance methods:
    __str__: prints the class name, id and creates dictionary
    representation of the input values
    save(self): updates instance instance attributes with current datetime
    to_dict: returns the dictionary values of the instance obj

    """

    def __init__(self, args, **kwargs):
        """Public instance attribute intitialization
        after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attribute values

        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.item():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, time_format)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing
        all keys/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class.__name__
        return map_objects
