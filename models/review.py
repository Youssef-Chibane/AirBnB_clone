#!/usr/bin/python3
""" Class review that inherits from base model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherits from base model """
    place_id = ""
    user_id = ""
    text = ""
