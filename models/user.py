#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from baseModel"""
    def __init__(self, email='',
                 password='',
                 first_name='',
                 last_name=''):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
