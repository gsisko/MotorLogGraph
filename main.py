# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import frame_main

import logging
import logging.config
import os
import sys

import wx


class WxPythonDragDropTemplate(wx.App):
    def __init__(self):
        super(WxPythonDragDropTemplate, self).__init__()
        logger = logging.getLogger(__name__)
        app_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
        logging.config.fileConfig(app_path + 'log_debug_to_terminal.ini', disable_existing_loggers=False)
        self.frame = frame_main.FrameMain(None)
        self.SetTopWindow(self.frame)
        logger.debug('Main: Loading GUI.')
        self.frame.Show()


if __name__ == '__main__':
    app = WxPythonDragDropTemplate()
    app.MainLoop()
    sys.exit()
