#!/usr/bin/python3
"""[summary]
"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            str1 = obj.__class__.__name__ + "." + obj.id
            self.__objects[str1] = obj

    def save(self):
        """Newdict = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w") as myFile:
            myFile.write(Newdict)"""
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    # Separate name_class from id and split the separator
                    k = key.split('.')
                    # search "__class__": "BaseModel"
                    class_name = k[0]
                    # set in __objects the key, value
                    self.new(eval("{}".format(class_name))(**value))
