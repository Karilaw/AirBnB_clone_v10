#!/usr/bin/python3
""" Place Module for HBNB project """
import uuid
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a new Place object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): A unique identifier for the Place object.
            city_id (str): The ID of the city associated with the Place.
            user_id (str): The ID of the user associated with the Place.
            name (str): The name of the Place.
            number_rooms (int): The number of rooms in the Place.
            number_bathrooms (int): The number of bathrooms in the Place.
            max_guest (int): The maximum number of guests the Place can accommodate.
            price_by_night (int): The price per night to stay at the Place.
            latitude (float): The latitude coordinate of the Place's location.
            longitude (float): The longitude coordinate of the Place's location.
            created_at (datetime): The timestamp when the Place was created.
            updated_at (datetime): The timestamp when the Place was last updated.

        Note:
            If an 'id' is not provided in the 'kwargs' dictionary, a new unique 'id'
            will be generated using 'uuid.uuid4()'.
        """
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
