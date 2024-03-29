#!/usr/bin/python3
"""
state module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines attributes/methods for the State class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
