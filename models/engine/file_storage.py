#!/usr/bin/python3
"""
Class of stroage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return FileStorage.__file_path

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
                for key in obj:
                    FileStorage.__objects[key] = BaseModel(**obj[key])
        except Exception:
            pass
