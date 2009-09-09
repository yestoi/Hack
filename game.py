import cmd

class Game:
    
    def __init__(self):
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

class CmdInterface(cmd.Cmd):
    """Main commandline interface"""
    
    def __init__(self, Game):
        cmd.Cmd.__init__(self)
        self.prompt = '# ' 
        self.game = Game

       # INPUT 
    def do_ls(self, line):
        input = line.split()

        if len(input) == 1:
            print "not implemented"
        else:
            self.game.ls()

    def do_pwd(self, line):
        self.game.pwd()

    def do_exit(self, line):
        return 1 

    def do_EOF(self, line):
        print "\n"
        return 0 #ignore EOFs
