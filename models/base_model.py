#!/usr/bin/python3
import uuid
import datetime


class BaseModel():

    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        string = '[{}] ({}) {}'.\
            format(self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        format_1 = "%Y-%m-%dT%H:%M:%S.%f"
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = self.__class__.__name__
        dict_1['created_at'] = dict_1['created_at'].strftime(format_1)
        dict_1['updated_at'] = dict_1['updated_at'].strftime(format_1)
        return dict_1
