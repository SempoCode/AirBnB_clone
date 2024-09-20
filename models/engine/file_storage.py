#!/usr/bin/python3
"""
FileStorage Module for the AirBnB clone project
"""
import json
from models.user import User  # Import User class
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary of all objects, or objects of a specific
        class if provided"""
        if cls:
            filtered_objs = {
                    k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
            return filtered_objs
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "User":
                        self.__objects[key] = User(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass


# Initialize storage as a FileStorage object
storage = FileStorage()
storage.reload()
