#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """stores files with JSON format"""

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the privect attribute __object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open("file.json", 'w', encoding="UTF-8") as f:
            f.write(json.dumps(objdict))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing. If the
            file doesn’t exist, no exception should be raised)
        """
        try:
            with open("file.json", 'r', encoding="UTF-8") as g:
                words = g.read()
                if words:
                    objdict = json.loads(words)
                    for o in objdict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
