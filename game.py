import cmd

class Game:
    """Main game logic. Where the shit happens""" 
    def __init__(self, Cli):
        self.cli = Cli

        #TODO Temporary solution to loading dicts. Switch to shelve when finished
        import yaml
        file = open('hosts.yml')
        self.hosts = yaml.safe_load(file)
        file.close()

        self.host = "localhost"
        self.user = ""
        self.printwd = "/"

    def ls(self):
        print "\n".join(self.hosts[self.host]['files'].keys())

    def pwd(self):
        print self.printwd 

    def telnet(self, host):
        #TODO: think of something else
        if (host == "contract.bbs.net"):
            print "Contracts"
    
    def clear(self):
        self.cli.cls = 1

class CmdInterface(cmd.Cmd):
    """Main commandline interface"""
    
    def __init__(self, Game, Cli):
        cmd.Cmd.__init__(self)
        self.prompt = '# ' 
        self.game = Game
        self.cli = Cli

       # INPUT 
    def do_ls(self, line):
        input = line.split()

        if len(input) == 1:
            print "not implemented"
        else:
            self.game.ls()

    def do_pwd(self, line):
        self.game.pwd()

    def do_telnet(self, line):
        self.game.telnet(line)

    def do_exit(self, line):
        return 1 

    def do_EOF(self, line):
        print "\n"
        return 0 #ignore EOFs
    
    def do_clear(self, line):
        self.game.clear()

        # RENDER
    def postcmd(self, stop, line):
        # So far we just need to clear the screen
        if self.cli.cls != 0:
            self.cli.clear()
        return stop

class CursesInterface:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.cls = 0

    def clear(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        self.cls = 0

    # IO hookup
    def write(self, line):
        self.stdscr.addstr(line)
        self.stdscr.refresh()
    def readline(self):
        return self.stdscr.getstr()



