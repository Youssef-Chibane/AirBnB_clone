#!/usr/bin/env pyhton3

""" this is the base for all my models"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ this is the base class for all my classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string repr of the object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
