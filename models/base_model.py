#!/usr/bin/python3
"""
Parent class for the entire project
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    def __init__(self):
        """Public instance attributes initialization

        Args:
            *args(args): arguments
            **kwargs(dict): attribute values

        """
        self.name = "Kamal"
        self.my_number = "11"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the class
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method returns a dictionary containing
        all keys/values of __dict__ instance.
        """
        map_objects = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__

        return map_objects