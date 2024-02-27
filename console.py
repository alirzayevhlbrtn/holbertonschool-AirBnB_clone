#!/usr/bin/python3
"""
Console of HBNB
"""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Class of console
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Handling quit in cmd
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        Handling EOF
        """
        return True

    def do_help(self, args):
        """
        Handling help
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Passing empty line
        """
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return
        arglist = args.split()
        class_name = arglist[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if class_name == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return
        arglist = args.split()
        class_name = arglist[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arglist) < 2:
            print("** instance id missing **")
            return
        ins_id = arglist[1]
        key = "{}.{}".format(class_name, ins_id)
        all_ins = BaseModel.to_dict()
        if key in all_ins:
            print(all_ins[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        arglist = args.split()
        class_name = arglist[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arglist) < 2:
            print("** instance id missing **")
            return
        insid = arglist[1]
        key = "{}.{}".format(class_name, ins_id)
        all_ins = BaseModel.to_dict()
        if key in all_ins:
            del all_ins[key]
            BaseModel.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, args):
        all_ins = BaseModel.to_dict()
        arglist = args.split()
        class_name = arglist[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        elif not args or class_name == "BaseModel":
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
