#!/usr/bin/python

# cmdline_fluency_countdown.py

import pickle # used to save user progress (currently supporting 1 primary user)
import ConfigParser, os # used to parse language file

def init():
	state = 0

	try:
		pickle.load(open("save.p", "rb"))
		print "SUCCESS: loaded save file!"
		state = 1

	except:
		config = ConfigParser.ConfigParser()
		config.read('lang.cfg')
		print "WELCOME: no save file found!"
		print "Type a [language] you want to learn (example: English),"
		print " or [list] then press [ENTER]"	
		selected_lang = raw_input()

		# joke
		if selected_lang == "English":
			print "You already know English!"
			quit()
		elif selected_lang == "list":
			list(selected_lang, config)
		elif selected_language == 

def list(what, cp):
	if what == "list":
		print "list what? [all] [easy] [medium] [hard] [other] [about]"
		selected_lang = raw_input()
		if selected_lang == "all":
			list1(cp)
			list2(cp)
			list3(cp)
			listo(cp)
		elif selected_lang == "easy":
			list1(cp)
		elif selected_lang == "medium":
			list2(cp)
		elif selected_lang == "hard":
			list3(cp)
		elif selected_lang == "other":
			listo(cp)
		elif selected_lang == "about":
			print "Coded by Houston Hunt"
			print "Times to mastering a language for English speakers"
			print "is given by " + str(cp.get('Reference', 'reference'))

def list1(cp):
	print cp.get('Languages', 'desc1')
	print str(cp.get('Languages', 'cat1'))

def list2(cp):
	print str(cp.get('Languages', 'desc2'))
	print str(cp.get('Languages', 'cat2'))

def list3(cp):
	print str(cp.get('Languages', 'desc3'))
	print str(cp.get('Languages', 'cat3'))

def listo(cp):
	print str(cp.get('Languages', 'desco'))
	print str(cp.get('Languages', 'other'))

init()
