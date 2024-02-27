#!/usr/bin/python3
"""
Console of HBNB
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
