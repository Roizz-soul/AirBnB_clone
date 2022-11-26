#!/usr/bin/python3
"""This module is for the command Interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The console class for the interpreter"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Makes the interpreter not to execute anything if the line
            is empty or if ENTER is typed only
        """
        pass
    def do_EOF(self, line):
        """EOF signals end of file and quits the command interpreter"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
