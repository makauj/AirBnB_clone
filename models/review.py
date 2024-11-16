#!/usr/bin/python3
"""State class"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place


class Review(BaseModel):
    """Review class"""
    
    def __init__(self):
        """initialize a new intance of Review"""
        self.place_id = Place.id
        self.user_id = User.id
        self.text = str('')