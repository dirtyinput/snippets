#!/usr/bin/env python

W = '\033[0m'  #white
R = '\033[31m' #red
G = '\033[32m' #green

def logprint(s):
	print '['+G+'-'+W+'] '+G+s+W

def logerror(s):
	print '['+R+'!'+W+'] '+R+s+W

logprint("TEsting")
logerror("THERE WAS AN ERROR")
