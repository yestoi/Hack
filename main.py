#!/usr/bin/python
import curses
import sys
import atexit
from game import Game, CmdInterface, CursesInterface

#TODO: Structure classes. Add docs. Start rolling

if __name__ == '__main__':

    stdscr = curses.initscr()
    #atexit.register(curses.endwin)
    curses.echo()

    cli = CursesInterface(stdscr)
    sys.stdout = cli
    sys.stdin = cli 
    sys.stderr = cli 

    g = Game(cli)

    Cmd = CmdInterface(g, cli)
    Cmd.cmdloop()
