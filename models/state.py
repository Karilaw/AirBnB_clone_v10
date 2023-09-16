#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = "Some State Name"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())

    def __str__(self):
        return "State {}: {}".format(self.id, self.name)
