#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
import os


class HBNBCommand(cmd, Cmd):
    """command line interpreter"""
    
    prompt = '(hbnb)'
    
    def quit(self, arg):
        """quit the command line interpreter"""
        return True
    
    def do_EOF(self, arg):
        """Exit cmd on EOF"""
        return True
    
    def do_help(self, arg):
        """Custom help for AirBnB project"""
        super().do_help(arg)
    
    def emptylibe(self):
        """Override emptyline method to prevent execution of empty commands"""
        pass
    
    def default(self, arg):
        """Handle default case when an unknown command is entered"""
        print(f"*** Unknown syntax: {arg}")
        



if __name__ == "__main__":
    HBNBCommand().cmdloop()