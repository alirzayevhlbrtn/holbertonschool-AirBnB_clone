#!/usr/bin/python3
"""
Console of HBNB
"""
import cmd
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Class of console
    """
    prompt = "(hbnb) "
    classdic = {"BaseModel": BaseModel}

    @staticmethod
    def isfloat(n):
        try:
            float(n)
            return True
        except ValueError:
            return False

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
        if class_name not in HBNBCommand.classdic.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classdic[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return
        arglist = args.split()
        class_name = arglist[0]
        if class_name not in HBNBCommand.classdic.keys():
            print("** class doesn't exist **")
            return
        if len(arglist) < 2:
            print("** instance id missing **")
            return
        ins_id = arglist[1]
        key = "{}.{}".format(class_name, ins_id)
        all_ins = models.storage.all()
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
        if class_name not in HBNBCommand.classdic.keys():
            print("** class doesn't exist **")
            return
        if len(arglist) < 2:
            print("** instance id missing **")
            return
        insid = arglist[1]
        key = "{}.{}".format(class_name, insid)
        if key in models.storage.all().keys():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, args):
        all_ins = models.storage.all()
        arglist = args.split()
        if not args:
            obj_list = list(map(lambda x: str(x), list(all_ins.values())))
            print(obj_list)
            return
        class_name = arglist[0]
        if class_name not in HBNBCommand.classdic.keys():
            print("** class doesn't exist **")
            return
        if class_name in HBNBCommand.classdic.keys():
            prlist = []
            for key in all_ins.keys():
                if class_name in str(key):
                    prlist.append(str(all_ins[key]))
            print(prlist)

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return
        arglist = args.split()
        if len(arglist) < 2:
            print("** instance id missing **")
            return
        if len(arglist) < 3:
            print("** attribute name missing **")
            return
        if len(arglist) < 4:
            print("** value missing **")
            return

        class_name = arglist[0]
        if class_name not in HBNBCommand.classdic.keys():
            print("** class doesn't exist **")
            return

        ins_id = arglist[1]
        key = "{}.{}".format(class_name, ins_id)
        all_ins = models.storage.all()
        if key not in all_ins:
            print("** no instance found **")
            return

        value = arglist[3]
        i = value.isdigit()
        d = HBNBCommand.isfloat(value)

        if i:
            setattr(all_ins[key], arglist[2], int(arglist[3]))
        elif d and not i:
            setattr(all_ins[key], arglist[2], float(arglist[3]))
        else:
            setattr(all_ins[key], arglist[2], arglist[3].strip('"'))

        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
