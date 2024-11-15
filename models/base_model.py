#!/usr/bin/python3
"""Base model for the AirBnB clone Console"""


import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return a string representative of the object class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__
                                     )

    def save(self):
        """updates the public attribute
        `updated_at` with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
