#!/usr/bin/python3
"""[summary]
"""
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        str1 = self.__class__.__name__ + "." + obj.id
        self.__objects[str1] = obj.to_dict()

    def save(self):
        Newdict = json.dumps(self.__objects)
        with open(self.__file_path, "w") as myFile:
            myFile.write(Newdict)

    def reload(self):
        if not os.path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, "rt") as myFile:
                self.__objects = json.loads(myFile.read())

