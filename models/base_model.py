#!/usr/bin/python3
""" Create class Base Model
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ this is the Father class for all the project
    """
    def __init__(self, *args, **kwargs):
        """ Main Contructor to contain the rules primary
        """
        format_1 = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, format_1)
                elif key == "created_at":
                    value = datetime.strptime(value, format_1)
                elif key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            # if is a new instance
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """Return a dict with attributes
        """
        format_1 = "%Y-%m-%dT%H:%M:%S.%f"
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = self.__class__.__name__
        dict_1['created_at'] = dict_1['created_at'].strftime(format_1)
        dict_1['updated_at'] = dict_1['updated_at'].strftime(format_1)
        return dict_1
