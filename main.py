#!/usr/bin/python
import curses
import sys
import atexit
from game import CmdInterface, Game

#TODO: Structure classes. Add docs. Start rolling

class FakeIO:
    def __init__(self):
        global stdscr
    def write(self, line):
        stdscr.addstr(line)
        stdscr.refresh()
    def readline(self):
        return stdscr.getstr()

if __name__ == '__main__':

    stdscr = curses.initscr()
    atexit.register(curses.endwin)
    curses.echo()

    f = FakeIO()
    sys.stdout = f
    sys.stdin = f
    sys.stderr = f
    
    g = Game()

    Cmd = CmdInterface(g)
    Cmd.cmdloop()
