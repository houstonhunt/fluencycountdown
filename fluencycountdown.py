#!/usr/bin/env python

# fluencycountdown.py

import wx
import ConfigParser

class MainWindow(wx.Frame):

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(250,150))

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
		self.Show(True)

		# create sizers
		vSizer = wx.BoxSizer(wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)

		# create static text
		self.staticText = wx.StaticText(self, wx.ID_ANY, "Pick a Language:", wx.DefaultPosition, wx.DefaultSize, 0)
		self.staticText.Wrap(-1)
		hSizer.Add(self.staticText, 0, wx.ALL, 5)

		choice_list = ['Afrikaans', 'Catalan']
		self.choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_list, 0) 
		hSizer.Add(self.choice, 0, wx.ALL, 5)

		self.SetSizer(vSizer)
		self.SetSizer(hSizer)
		self.Layout()
		self.Centre(wx.BOTH)
		
		# drop down list
		self = wx.Choice(self, -1, (100, 100), (75, -1))

app = wx.App(False)
frame = MainWindow(None, "Fluency Countdown")
app.MainLoop()

