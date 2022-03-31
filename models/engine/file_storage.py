#!/usr/bin/python3
"""
Contains the class called FileStorage
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    serializes instances to a JSON file and de-'s back to instances
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects into JSON file (path: __file_path)
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete the obj from __objects if inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        calls the reload() method, deserializing the JSON file to obj's'
        """
        self.reload()

    def get(self, cls, id):
        """
        This method retrieves one object
        """
        for values in self.all(cls).values():
            if values.id == id:
                return values
        return None

    def count(self, cls=None):
        """
        a method to count number of objects in the storage
        """
        if cls is None:
            return len(self.all())
        else:
            return len(self.all(cls))
