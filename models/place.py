#!/usr/bin/python3
"""Place class"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity


class Place(BaseModel):
    """Place class"""
    
    def __init__(self):
        """initialize a new Place model"""
        self.city_id = City.id
        self.user_id = User.id
        self.name = ''
        self.description = ''
        self.number_rooms = int('')
        self.number_bathrooms = int('')
        self.max_guest = int('')
        self.price_by_night = int('')
        self.latitude = float('')
        self.longitude = float('')
        self.amenity_ids = Amenity.id
