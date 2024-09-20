#!/usr/bin/python3
"""
FileStorage module that serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {
                key: obj.to_dict() 
                for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value['__class__']
                # Check for the class name and instantiate objects
                if class_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
                elif class_name == "User":
                    FileStorage.__objects[key] = User(**value)
                elif class_name == "State":
                    FileStorage.__objects[key] = State(**value)
                elif class_name == "City":
                    FileStorage.__objects[key] = City(**value)
                elif class_name == "Amenity":
                    FileStorage.__objects[key] = Amenity(**value)
                elif class_name == "Place":
                    FileStorage.__objects[key] = Place(**value)
                elif class_name == "Review":
                    FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
