#!/usr/bin/python3
"""
Class of stroage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __c = {"BaseModel": BaseModel,
             "User": User,
             "Review": Review,
             "State": State,
             "City": City,
             "Amenity": Amenity,
             "Place": Place}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        FileStorage.__objects = value

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        new = {}
        for key, value in FileStorage.__objects.items():
            new[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as wf:
            json.dump(new, wf)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as rf:
                obj = json.load(rf)
                for k in obj:
                    name = k.split(".")[0]
                    FileStorage.__objects[k] = FileStorage.__c[name](**obj[k])
        except Exception:
            pass
