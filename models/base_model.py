#!/usr/bin/python3
"""
Base Model module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class
    """
    def __init__(self, *args, **kwargs):
        """
        Init function
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%5.%f')
                if key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """
        Str function
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        Save function
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
