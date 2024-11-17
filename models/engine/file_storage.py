#!/usr/bin/python3
"""
file storage class
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage():
    """Class that searializes instances to JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Method serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: obj.to_dict() for key,
                       obj in self.__objects.items()}, f)

    def reload(self):
        """Method to deserialize JSON file to objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    
                    class_mapping = {
                        'BaseModel': BaseModel,
                        'user': User,
                        'state': State,
                        'review': Review,
                        'place': Place,
                        'city': City,
                        'amenity': Amenity
                    }

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")

                        cls = eval(class_name)
                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
