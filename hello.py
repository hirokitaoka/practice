#!/usr/bin/env python

def hello(name):
    print "Hello " + name + "!"
    return

def bye(name):
    print "Bye " + name + "!"
    return

fh = open("namelist.txt", "r")

for name in  fh.readlines():
    hello(name.strip())
    bye(name.strip())
