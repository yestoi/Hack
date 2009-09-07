import cmd
import readline #for bash-like history

class Game:
    
    def __init__(self):
        import yaml
        file = open('hosts.yml')
        self.hosts = yaml.safe_load(file)
        file.close()

        self.curr_host = "localhost"

    def ls(self):
        print self.hosts[self.curr_host]['files'].keys()
        

class CmdInterface(cmd.Cmd):
    """Main commandline interface"""
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '# ' 
        self.Game = Game()

       # COMMANDS
    def do_ls(self, line):
        input = line.split()
        if len(input) == 1:
            print "not implemented"
        else:
            self.Game.ls()

    def do_exit(self, line):
        return 1 

    def do_EOF(self, line):
        return 0 #ignore EOFs
