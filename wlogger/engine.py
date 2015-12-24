"""The engine module of wlogger"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import datetime
import os
import sys
import time
import pickle

home = os.path.expanduser("~")


def engine() :
	""" Sets the directory """

	if not os.path.exists(home + '/.wloggerconfig') :
		newuser()
	
	location = extract_path()
	return location


def newuser() :
	""" 
		Setup new-user :

		Creates a file `.wloggerconfig` inside home folder

	"""

	config_file = open(home + '/.wloggerconfig' , 'w')
	config_file.write('[location]\n\t' + os.getcwd() + '\n')
	config_file.close()
	todo = dict()
	done = dict()
	pickle.dump(todo, open(os.getcwd()  + '/wlogger/data/todo.p', 'wb'))
	pickle.dump(done, open(os.getcwd() + '/wlogger/data/done.p', 'wb'))
	open(os.getcwd()  + '/wlogger/data/wlog.txt', 'w').close()
	open(os.getcwd()  + '/wlogger/data/wlog.md', 'w').close()
	open(os.getcwd()  + '/wlogger/data/wlog.html', 'w').close()

def reconfig() :
	"""
		Reset user package
	"""
	if os.path.exists(home + '/.wloggerconfig') :
		location = extract_path()
		os.remove(home+'/.wloggerconfig')
		newuser()

def extract_path() :
	
	"""Return the path where log is stored locally"""

	f = open(home + '/.wloggerconfig', 'r')
	location = ""
	next_one = False  # If true then the next line contains our result
	for line in f.readlines():
		if next_one is True:
			location = line.lstrip().rstrip()
			break
		elif line == "[location]\n":
		    next_one = True
	f.close()
	if location == "":
	    sys.stderr.write("'$HOME/.wloggerconfig' file seems to be missing.")
	    sys.exit(2)
	else:
	    return location