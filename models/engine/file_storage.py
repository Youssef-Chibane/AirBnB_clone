#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict_file = json.load(file)
                for cl_id, To_obj in dict_file.items():
                    if "BaseModel" in cl_id:
                        FileStorage.__objects[cl_id] = BaseModel(**To_obj)
                    elif "User" in cl_id:
                        FileStorage.__objects[cl_id] = User(**To_obj)
                    elif "Place" in cl_id:
                        FileStorage.__objects[cl_id] = Place(**To_obj)
                    elif "State" in cl_id:
                        FileStorage.__objects[cl_id] = State(**To_obj)
                    elif "City" in cl_id:
                        FileStorage.__objects[cl_id] = City(**To_obj)
                    elif "Amenity" in cl_id:
                        FileStorage.__objects[cl_id] = Amenity(**To_obj)
                    elif "Review" in cl_id:
                        FileStorage.__objects[cl_id] = Review(**To_obj)
        except Exception:
            pass
