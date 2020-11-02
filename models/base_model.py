#!/usr/bin/python3
""" Create class Base Model
"""


import uuid
from datetime import datetime


class BaseModel():
    """ this is the Father class for all the project
    """
    def __init__(self, *args, **kwargs):
        """ Main Contructor to contain the rules primary
        """
        format_1 = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key is "created_at" and type(value) is str:
                        self.created_at = datetime.strptime(value, format_1)
                    elif key is "updated_at" and type(value) is str:
                        self.updated_at = datetime.strptime(value, format_1)
                    else:
                        setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

    def __str__(self):
        """ Return new representation of instance
        """
        string = '[{}] ({}) {}'.\
            format(self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        """ Update date time newest
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dict with attributes
        """
        format_1 = "%Y-%m-%dT%H:%M:%S.%f"
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = self.__class__.__name__
        dict_1['created_at'] = dict_1['created_at'].strftime(format_1)
        dict_1['updated_at'] = dict_1['updated_at'].strftime(format_1)
        return dict_1
