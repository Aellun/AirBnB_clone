#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent the class filestorage

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): a class attribute rep dict to store objects
        initialzed as empty
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary oject instantiated."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id
        contanating the objec id with with class name with a dot"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for item in objdict.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
