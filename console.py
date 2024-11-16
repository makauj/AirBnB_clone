#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
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

    def emptyline(self):
        """Override emptyline method to prevent execution of empty commands"""
        pass

    def default(self, arg):
        """Handle default case when an unknown command is entered"""
        print(f"*** Unknown syntax: {arg}")

    def create(self, arg):
        """Create a new instance of BaseModel"""
        commands = shlex.splir(arg)

        if len(commands) == 0:
            print(f"** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)
    
    def show(self, arg):
        """
        Print string representtion of an instance based on class, name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] is not "BaseModel":
                print("** instance id missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"BaseModel.{args[1]}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] is not "BaseModel":
                print("** class doesn't exits **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"BaseModel.{args[1]}"
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if arg and arg is not "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(',')[0] == commands[0]:
                    print(str(value))
    
    def do_count(self, arg):
        """Counts and ret"""



if __name__ == "__main__":
    HBNBCommand().cmdloop()
