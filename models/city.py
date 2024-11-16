#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel  # type: ignore


class City(BaseModel):
    """City Class"""
    def __init__(self, state_id, name=''):
        """initialize a new instance of City"""
        self.id = state_id
