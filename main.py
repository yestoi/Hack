#!/usr/bin/python
import curses
import sys
import atexit
from game import Game, CmdInterface, FakeIO

#TODO: Structure classes. Add docs. Start rolling

if __name__ == '__main__':

    stdscr = curses.initscr()
    #atexit.register(curses.endwin)
    curses.echo()

    f = FakeIO(stdscr)
    sys.stdout = f
    sys.stdin = f
    sys.stderr = f
    
    g = Game()

    Cmd = CmdInterface(g)
    Cmd.cmdloop()
