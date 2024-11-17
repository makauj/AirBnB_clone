#!/usr/bin/python3
"""entry point of the command interpreter"""

import ast
import cmd
import re
import shlex

from models import storage


def split_args(e_arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)

    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return "", {}
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if len(commands) >= 3:
            try:
                id = commands[0].strip()
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


class HBNBCommand(cmd.Cmd):
    """command line interpreter"""

    prompt = '(hbnb)'
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def do_quit(self, arg):
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

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print(f"** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = commands[0]
            if class_name in self.valid_classes:
                class_ = globals().get(class_name)
                if class_:
                    new_instance = class_()
                    storage.save()
                    print(new_instance.id)

    def do_show(self, arg):
        """
        Print string representtion of an instance based on class, name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.valid_classes:
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
            if args[0] not in self.valid_classes:
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

        if arg and arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(',')[0] == commands[0]:
                    print(str(value))

    def update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            class_name, instance_id = args[0], args[1]
            key = f"{class_name}.{instance_id}"
            if key not in storage.all():
                print("** no intance found **")
            elif len(args) < 3:
                print("** no instance found **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = objects[key]
                braces = re.search(r"\{(.*?)\}", arg)

                if braces:
                    try:
                        str_data = braces.group(1)
                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_name = list(arg_dict.keys())
                        attribute_value = list(arg_dict.values())
                        try:
                            attr_name0 = attribute_name[0]
                            attr_val0 = attribute_value[0]
                            setattr(instance, attr_name0, attr_val0)
                        except Exception:
                            pass

                        try:
                            attr_name1 = attribute_name[1]
                            attr_val1 = attribute_value[1]
                            setattr(instance, attr_name1, attr_val1)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    attr_name = args[2]
                    attr_val = args[3]
                    try:
                        attr_val = eval(attr_val)
                    except Exception:
                        pass
                    setattr(instance, attr_name, attr_val)

        instance.save()

    def default(self, arg):
        """Handle default case when an unknown command is entered"""
        arg_list = arg.split('.')
        class_name = arg_list[0]
        command = arg_list[1].split('(')
        cmd_method = command[0]
        extra_arg = command[1].split(')')[0]

        method_dict = {
            'quit': self.do_quit,
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_show,
            'update': self.update,
            'count': self.do_count,
            'create': self.do_create
        }
        if cmd_method in method_dict.keys():
            if cmd_method != 'update':
                return (method_dict[cmd_method]
                        (f"{class_name} {extra_arg}"))
            else:
                if not class_name:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_args(extra_arg)
                    call = method_dict[cmd_method]
                    return call(f"{class_name} {obj_id} {arg_dict}")
                except Exception:
                    pass
        else:
            print(f"** Unknown syntax: {arg} **")
            return False

    def do_count(self, arg):
        """Counts and returns number of instances of a class"""
        objs = storage.all()
        commands = shlex.split(arg)

        if not arg:
            print("** class name missing **")
            return

        cls_name = commands[0]
        if cls_name in self.valid_classes:
            count = sum(1 for obj in objs.values()
                        if obj.__class__.__name__ == cls_name)
            print(count)
        else:
            print("** invalid class name **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
