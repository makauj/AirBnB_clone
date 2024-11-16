#!/usr/bin/python3
"""amenity class"""

from models.base_model import BaseModel # type: ignore


class Amenity(BaseModel):
    """Amenity class"""
    
    def __init__(self, name=''):
        """initialize a new amenity instance"""
        self.name = name
