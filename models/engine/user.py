#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines attributes/methods for the User class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
