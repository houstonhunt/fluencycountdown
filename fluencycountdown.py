#!/usr/bin/env python

# fluencycountdown.py

import wx
import datetime
import time
import ConfigParser
import ast # for parsing in list data structure from config file
from functools import partial

class MainWindow(wx.Frame):

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(325,150))
		self.time2fluency = 0

		self.InitUI()

	def InitUI(self):

		# setup config parser
		config = ConfigParser.ConfigParser()
		config.read('lang.cfg')

		# menu items setup
		fmenu = wx.Menu()
		fmenu.Append(wx.ID_ABOUT, "&About", "About Fluency Countdown")
		fmenu.AppendSeparator()
		fmenu.Append(wx.ID_OPEN, "&Open", "Open Save File")

		# menu bar creation
		menuBar = wx.MenuBar()
		menuBar.Append(fmenu, "&File")
		self.SetMenuBar(menuBar)

		# create sizers
		self.vSizer = wx.BoxSizer(wx.VERTICAL)
		self.hSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.hSizer2 = wx.BoxSizer(wx.HORIZONTAL)

		# create static text
		self.staticText = wx.StaticText(self, wx.ID_ANY, "Pick a Language:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
		self.staticText.Wrap(-1)
		self.hSizer.Add(self.staticText, 0, wx.ALL, 5)

		# populate choice list from config file
		choice_list = []
		choice_list.append('')
		choice_list.append('--category 1--')
		choice_list.extend(ast.literal_eval(config.get('Languages', 'cat1')))
		choice_list.append('--category 2--')
		choice_list.extend(ast.literal_eval(config.get('Languages', 'cat2')))
		choice_list.append('--category 3--')
		choice_list.extend(ast.literal_eval(config.get('Languages', 'cat3')))
		choice_list.append('-- other --')
		choice_list.extend(ast.literal_eval(config.get('Languages', 'other')))

		# add choice to window
		self.choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_list, 0) 
		self.choice.Bind(wx.EVT_CHOICE, partial(self.onChoice, conf = config))
		self.hSizer.Add(self.choice, 0, wx.ALL, 5)

		self.vSizer.Add(self.hSizer, 1, wx.ALIGN_CENTER, 5)
		
		# add language time to completion text
		self.staticText2 = wx.StaticText(self, wx.ID_ANY, "Estimated time: hrs", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
		self.staticText2.Wrap(-1)
		self.vSizer.Add(self.staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.textlang = wx.StaticText(self, wx.ID_ANY, "",wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
		self.textlang.Wrap(-1)

		# create timer
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)

		# add button
		self.start_stop_button = wx.Button(self, wx.ID_ANY, "Start", wx.DefaultPosition, wx.DefaultSize, 0)
		self.start_stop_button.Bind(wx.EVT_BUTTON, self.startStop)
		self.vSizer.Add(self.start_stop_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.SetSizer(self.vSizer)
		self.Layout()

		self.Centre(wx.BOTH)
		self.Show(True)

	# language picked
	def onChoice(self, event, conf):
		choice = self.choice.GetStringSelection()
		#self.hSizer.ShowItems(0)
		#self.textlang.SetLabel(choice)
		self.Layout()
		if conf.get('Languages', 'cat1').find(choice) != -1: 
			self.staticText2.SetLabel(conf.get('Languages', 'desc1'))
			self.time2fluency = datetime.timedelta(hours=600)
		elif conf.get('Languages', 'cat2').find(choice) != -1: 
			self.staticText2.SetLabel(conf.get('Languages', 'desc2'))
			self.time2fluency = datetime.timedelta(hours=1100)
		elif conf.get('Languages', 'cat3').find(choice) != -1: 
			self.staticText2.SetLabel(conf.get('Languages', 'desc3'))
			self.time2fluency = datetime.timedelta(hours=2200)
		elif conf.get('Languages', 'other').find(choice) != -1: 
			self.staticText2.SetLabel(conf.get('Languages', 'desco'))
			self.time2fluency = datetime.timedelta(hours=900)
		else:
			self.staticText2.SetLabel("")
		self.Layout()

	def startStop(self, event):
		if self.timer.IsRunning():
			self.timer.Stop()
			self.start_stop_button.SetLabel("Start")
		else:
			self.timer.Start()
			self.start_stop_button.SetLabel("Pause")

	def update(self, event):
		self.staticText2.SetLabel(str(self.time2fluency))
		self.time2fluency = self.time2fluency  - datetime.timedelta(seconds=1)

app = wx.App(False)
frame = MainWindow(None, "Fluency Countdown")
app.MainLoop()
