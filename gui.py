# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.DragDropPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
		self.DragDropPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		PanelSizer = wx.BoxSizer( wx.VERTICAL )
		
		
		PanelSizer.AddSpacer( ( 0, 35), 0, 0, 0 )
		
		
		PanelSizer.AddSpacer( ( 0, 25), 0, 0, 0 )
		
		self.DropHereStaticText = wx.StaticText( self.DragDropPanel, wx.ID_ANY, _(u"Drop files here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.DropHereStaticText.Wrap( -1 )
		self.DropHereStaticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		PanelSizer.Add( self.DropHereStaticText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )
		
		self.OrBrowseStaticText = wx.StaticText( self.DragDropPanel, wx.ID_ANY, _(u"or"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OrBrowseStaticText.Wrap( -1 )
		PanelSizer.Add( self.OrBrowseStaticText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.BrowseButton = wx.Button( self.DragDropPanel, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
		PanelSizer.Add( self.BrowseButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )
		
		
		self.DragDropPanel.SetSizer( PanelSizer )
		self.DragDropPanel.Layout()
		MainSizer.Add( self.DragDropPanel, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.ProgressGaugePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
		self.ProgressGaugePanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.ProgressGaugePanel.Hide()
		
		PanelSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.ProgressText = wx.StaticText( self.ProgressGaugePanel, wx.ID_ANY, _(u"Please wait ..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ProgressText.Wrap( -1 )
		PanelSizer.Add( self.ProgressText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.ProgressGauge = wx.Gauge( self.ProgressGaugePanel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.ProgressGauge.SetValue( 0 ) 
		PanelSizer.Add( self.ProgressGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.ProgressGaugePanel.SetSizer( PanelSizer )
		self.ProgressGaugePanel.Layout()
		MainSizer.Add( self.ProgressGaugePanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.ProgressMultiGaugePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
		self.ProgressMultiGaugePanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.ProgressMultiGaugePanel.Hide()
		
		PanelSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.ProgressPartStaticText = wx.StaticText( self.ProgressMultiGaugePanel, wx.ID_ANY, _(u"Processing file x/y"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ProgressPartStaticText.Wrap( -1 )
		PanelSizer.Add( self.ProgressPartStaticText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.ProgressOneGauge = wx.Gauge( self.ProgressMultiGaugePanel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.ProgressOneGauge.SetValue( 0 ) 
		PanelSizer.Add( self.ProgressOneGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ProgressTotalStaticText = wx.StaticText( self.ProgressMultiGaugePanel, wx.ID_ANY, _(u"Total Progress"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ProgressTotalStaticText.Wrap( -1 )
		PanelSizer.Add( self.ProgressTotalStaticText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.ProgressTwoGauge = wx.Gauge( self.ProgressMultiGaugePanel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.ProgressTwoGauge.SetValue( 0 ) 
		PanelSizer.Add( self.ProgressTwoGauge, 0, wx.ALL, 5 )
		
		
		self.ProgressMultiGaugePanel.SetSizer( PanelSizer )
		self.ProgressMultiGaugePanel.Layout()
		MainSizer.Add( self.ProgressMultiGaugePanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.ProgressGifPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
		self.ProgressGifPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.ProgressGifPanel.Hide()
		
		PanelSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		PanelSizer1.AddSpacer( ( 0, 50), 0, 0, 0 )
		
		self.WaitStaticText = wx.StaticText( self.ProgressGifPanel, wx.ID_ANY, _(u"Please wait ..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WaitStaticText.Wrap( -1 )
		PanelSizer1.Add( self.WaitStaticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.ProgressGifPanel.SetSizer( PanelSizer1 )
		self.ProgressGifPanel.Layout()
		MainSizer.Add( self.ProgressGifPanel, 0, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.DragDropPanel.Bind( wx.EVT_ERASE_BACKGROUND, self.add_drag_drop_panel_background )
		self.BrowseButton.Bind( wx.EVT_BUTTON, self.on_button_browse )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def add_drag_drop_panel_background( self, event ):
		event.Skip()
	
	def on_button_browse( self, event ):
		event.Skip()
	

