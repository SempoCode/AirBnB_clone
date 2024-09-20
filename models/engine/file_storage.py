import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects dictionary"""
        self.__objects[obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        obj_dict = {
                obj_id: obj.to_dict()
                for obj_id, obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                # If you have classes in the future, recreate objects here
        except FileNotFoundError:
            pass
