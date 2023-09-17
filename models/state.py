#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid


class State(BaseModel):
    """ State class """
    name = "Some State Name"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())

    def __str__(self):
        # Remove the '__class__' key from the dictionary
        state_dict = self.to_dict()
        state_dict.pop('__class__', None)

        # Reorder the dictionary so that 'id' comes first
        state_dict = {'id': state_dict.pop('id', None), **state_dict}

        return "[State] ({}) {}".format(self.id, state_dict)
