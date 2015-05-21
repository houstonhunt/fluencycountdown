#!/usr/bin/env python

# fluencycountdown.py

import wx
import ConfigParser
import ast # for parsing in list data structure from config file

class MainWindow(wx.Frame):

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(275,150))

		self.InitUI()

	def InitUI(self):
		# setup config parser
		config = ConfigParser.ConfigParser()
		config.read('lang.cfg')

		# main window text
		text1 = "Choose a Language you would like to learn"

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
		vSizer = wx.BoxSizer(wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)

		# create static text
		self.staticText = wx.StaticText(self, wx.ID_ANY, "Pick a Language:", wx.DefaultPosition, wx.DefaultSize, 0)
		self.staticText.Wrap(-1)
		hSizer.Add(self.staticText, 0, wx.ALL, 5)

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
		hSizer.Add(self.choice, 0, wx.ALL, 5)

		vSizer.Add(hSizer, 1, wx.ALIGN_CENTER, 5)
		
		# add language time to completion text
		self.staticText2 = wx.StaticText(self, wx.ID_ANY, "Estimated time: 2200 hrs", wx.DefaultPosition, wx.DefaultSize, 0)
		self.staticText2.Wrap(-1)
		vSizer.Add(self.staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		# add button
		self.start_pause_button = wx.Button(self, wx.ID_ANY, "Start", wx.DefaultPosition, wx.DefaultSize, 0)
		vSizer.Add(self.start_pause_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.SetSizer(vSizer)
		self.Layout()

		self.Centre(wx.BOTH)
		self.Show(True)

app = wx.App(False)
frame = MainWindow(None, "Fluency Countdown")
app.MainLoop()

