#!/usr/bin/python3
"""
This module implements the command interpreter for the AirBnB clone project.

It uses the cmd module to create an interactive shell that allows users to
create,
update, destroy, and display instances of BaseModel and other classes in the
project.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class that extends cmd.Cmd for the AirBnB clone.
    
    Methods:
        do_create: Creates a new instance of a class.
        do_show: Displays an instance based on class name and id.
        do_destroy: Deletes an instance based on class name and id.
        do_all: Prints all string representations of all instances.
        do_update: Updates an instance by adding or updating an attribute.
        emptyline: Overrides default behavior to do nothing on empty input.
        do_quit: Exits the console.
        do_EOF: Handles the EOF signal to exit the console.
    """
    
    prompt = '(hbnb) '

    def do_create(self, args):
        """
        Creates a new instance of BaseModel and prints its id.
        
        Usage: create <class name>
        
        Args:
            args (str): The name of the class to create.
            
        Example:
            (hbnb) create BaseModel
        """
        if not args:
            print("** class name missing **")
        elif args not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        class name and id.
        
        Usage: show <class name> <id>
        
        Args:
            args (str): The class name and id of the instance to show.
            
        Example:
            (hbnb) show BaseModel 1234-5678-9012
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id, and updates
        the JSON file.
        
        Usage: destroy <class name> <id>
        
        Args:
            args (str): The class name and id of the instance to destroy.
            
        Example:
            (hbnb) destroy BaseModel 1234-5678-9012
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representations of all instances, optionally
        based on class name.
        
        Usage: all [<class name>]
        
        Args:
            args (str): Optional class name to filter results.
            
        Example:
            (hbnb) all BaseModel
            (hbnb) all
        """
        objs = storage.all()
        obj_list = []
        if not args:
            for obj in objs.values():
                obj_list.append(str(obj))
        elif args in globals():
            for key, obj in objs.items():
                if key.startswith(args):
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, args):
        """
        Updates an instance by adding or updating attributes.
        
        Usage: update <class name> <id> <attribute name> "<attribute
        value>"
        
        Args:
            args (str): The class name, id, attribute name, and value to
            update.
            
        Example:
            (hbnb) update BaseModel 1234-5678-9012 first_name "Betty"
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                setattr(obj, arg_list[2], eval(arg_list[3]))
                obj.save()

    def emptyline(self):
        """Overrides default behavior to do nothing on empty input."""
        pass

    def do_quit(self, args):
        """Quits the console."""
        return True

    def do_EOF(self, args):
        """Handles the EOF signal to exit the console."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

