#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    
    prompt = "(hbnb) "  # Custom prompt
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()  # Start the command loop
