#!/usr/bin/python3
"""State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    
    def __init__(self, name=''):
        """Initialize a new instance of the class"""
        self.name = name
