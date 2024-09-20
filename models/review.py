#!/usr/bin/python3
"""
Review module that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for managing review information"""
    place_id = ""
    user_id = ""
    text = ""
