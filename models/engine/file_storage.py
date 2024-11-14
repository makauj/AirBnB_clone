#!/usr/bin/python3
"""
file storage class
"""

import json
import os
import uuid
from models.base_model import BaseModel


class FileStorage():
    """Class that searializes instances to JSON file"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Method serializes __objects to the JSON file"""

    def reload(self):
        """Method to deserialize JSON file to objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")

                        cls = eval(class_name)
                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
