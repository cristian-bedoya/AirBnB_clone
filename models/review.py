#!/usr/bin/python3
"""Module to add Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that inherit from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
