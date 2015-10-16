# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import mainframe

import sys

import wx


class WxPythonDragDropTemplate(wx.App):
    def __init__(self):
        super(WxPythonDragDropTemplate, self).__init__()
        self.frame = mainframe.MainFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()


if __name__ == '__main__':
    app = WxPythonDragDropTemplate()
    app.MainLoop()
    sys.exit()
