import cmd
import readline #for bash-like history

class Game:
    
    def __init__(self):
        # Temporary solution to loading dicts. Switch to shelve when finished
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

    def do_pwd(self, line):
        self.Game.pwd()

    def do_exit(self, line):
        return 1 

    def do_EOF(self, line):
        print "\n"
        return 0 #ignore EOFs
