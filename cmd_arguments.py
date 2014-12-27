#encoding:utf-8

import cmd

class Helloworld(cmd.Cmd):
    def do_greet(self,person):
        """greet [person]
        Greet the named person"""
        if person:
            print "hi,",person
        else:
            print "hi"

    def do_EOF(self,line):
        return True

    def postloop(self):
        print

if __name__=='__main__':
    Helloworld().cmdloop()
