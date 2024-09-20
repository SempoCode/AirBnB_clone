#!/usr/bin/python3
"""
City module that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class for managing city information"""
    state_id = ""
    name = ""
