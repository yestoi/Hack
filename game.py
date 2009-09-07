import cmd
import readline #for bash-like history

#class Game:
    #TODO: interface to load files using yaml


class CmdInterface(cmd.Cmd):
    """Main commandline interface"""

    #Startup of class
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.promt = '# ' 
        #game = Game()

    #Set up interface before cmdloop is called
    #def preloop(slef):
        #TODO: initalize ncurses
        

    # COMMANDS
    def do_ls(self, line):
        input = line.split()
        if len(input) == 1:
            print "not implemented"
        else:
            print "lookup files"

    def do_exit(self, line):
        return 1 #TODO: implement clean exit 

    def do_EOF(self, line):
        return 0 #ignore EOFs
