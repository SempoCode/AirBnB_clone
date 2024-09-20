#!/usr/bin/python3
"""
Console Module for the AirBnB Clone Project
This module provides a command-line interface to interact with the AirBnB
clone.
It allows users to create, show, update, destroy, and list User objects.
"""

import cmd
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create a new User instance and save it to the JSON file.
        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
            return
        if line != "User":
            print("** class doesn't exist **")
            return
        new_user = User()
        new_user.save()
        print(new_user.id)

    def do_show(self, line):
        """Show a User instance by its ID.
        Usage: show <class_name> <id>
        """
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        if args[0] != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        user_id = args[1]
        all_users = storage.all(User)
        key = f"User.{user_id}"
        if key not in all_users:
            print("** no instance found **")
            return
        print(all_users[key])

    def do_destroy(self, line):
        """Destroy a User instance by its ID.
        Usage: destroy <class_name> <id>
        """
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        if args[0] != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        user_id = args[1]
        all_users = storage.all(User)
        key = f"User.{user_id}"
        if key not in all_users:
            print("** no instance found **")
            return
        del all_users[key]
        storage.save()

    def do_update(self, line):
        """Update a User instance by its ID.
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = line.split()
        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
            return
        if args[0] != "User":
            print("** class doesn't exist **")
            return

        user_id = args[1]
        all_users = storage.all(User)
        key = f"User.{user_id}"
        if key not in all_users:
            print("** no instance found **")
            return

        setattr(all_users[key], args[2], args[3])
        all_users[key].save()

    def do_all(self, line):
        """Display all User instances.
        Usage: all <class_name> (optional)
        """
        if line and line != "User":
            print("** class doesn't exist **")
            return
        
        all_users = storage.all(User)
        for user in all_users.values():
            print(user)

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
