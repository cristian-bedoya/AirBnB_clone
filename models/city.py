#!/usr/bin/python3
"""Module to add City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ class City that inherit from BaseModel
    """
    state_id = ''
    name = ""
