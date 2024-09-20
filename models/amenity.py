#!/usr/bin/python3
"""
Amenity module that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for managing amenity information"""
    name = ""
