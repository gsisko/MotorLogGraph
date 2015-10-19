# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ErrorWarningDialog
###########################################################################

class ErrorWarningDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Error/Warning", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 500,250 ), wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		HeaderSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.HeaderStaticText = wx.StaticText( self, wx.ID_ANY, u"Error/Warning", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HeaderStaticText.Wrap( -1 )
		self.HeaderStaticText.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		HeaderSizer.Add( self.HeaderStaticText, 1, wx.ALL|wx.EXPAND, 8 )
		
		
		MainSizer.Add( HeaderSizer, 0, wx.EXPAND, 5 )
		
		self.DescriptionStaticText = wx.StaticText( self, wx.ID_ANY, u"An unhandled exception occurred. Please contact a developer if this behavior persists.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DescriptionStaticText.Wrap( -1 )
		MainSizer.Add( self.DescriptionStaticText, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.LogStaticText = wx.StaticText( self, wx.ID_ANY, u"This is the relevant section of the log:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LogStaticText.Wrap( -1 )
		MainSizer.Add( self.LogStaticText, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.LogTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"Feed the content of the log in here.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		MainSizer.Add( self.LogTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		OkButton = wx.StdDialogButtonSizer()
		self.OkButtonOK = wx.Button( self, wx.ID_OK )
		OkButton.AddButton( self.OkButtonOK )
		OkButton.Realize();
		
		MainSizer.Add( OkButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

