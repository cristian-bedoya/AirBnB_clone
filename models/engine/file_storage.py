#!/usr/bin/python3
"""Module to store all in Json file
"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """ Class File Storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Contain all object "Dictionary"
        """
        return self.__objects

    def new(self, obj):
        """Object dict file to save in Json
        """
        if obj:
            str1 = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[str1] = obj

    def save(self):
        """Save information in Json File
        """
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """ Deserialization information of Json file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    k = key.split('.')
                    class_name = k[0]
                    self.new(eval("{}".format(class_name))(**value))
