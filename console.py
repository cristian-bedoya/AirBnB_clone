#!/usr/bin/python3
""" Module for command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter
    """
    prompt = '(hbnb) '
    dict_classes = {"BaseModel":"BaseModel"}

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """ End of File

        Returns:
            true == exit
        """
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        if line == "" or line is None:
            print("{}".format("** class name missing **"))
        elif line not in self.dict_classes:
            print("{}".format("** class doesn't exist **"))
        else:
            New = BaseModel()
            New.save()
            print(New.id)

    def do_show(self, line):
        if line == "" or line is None:
            print("{}".format("** class name missing **"))
        else:
            list_line = line.split(' ')
            if list_line[0] not in self.dict_classes:
                print("{}".format("** class doesn't exist **"))
            elif len(list_line) < 2:
                print("{}".format("** instance id missing **"))
            else:
                objects = storage.all()
                key = list_line[0] + '.' + list_line[1]
                if key not in objects:
                    print("{}".format("** no instance found **"))
                else:
                    print("{}".\
                        format(objects[key]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
