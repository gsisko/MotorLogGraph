# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import dialog_errorwarning_gui

import platform
import logging
import logging.config
import os

import wx


# Logging config on sub-module level.
logger = logging.getLogger(__name__)


class ErrorWarningDialog(dialog_errorwarning_gui.ErrorWarningDialog):
    def __init__(self, parent, dialog_type, text):
        dialog_errorwarning_gui.ErrorWarningDialog.__init__(self, parent)
        logger.debug('Initializing ErrorWarningDialog (type "%s")' % dialog_type)
        self.CenterOnParent()
        self.Bind(wx.EVT_CLOSE, self.on_window_close)
        self.SetFocus()
        self.OkButtonOK.SetDefault()

        # Note "parent" is expected to be the (main) frame of the program, not some panel!
        self.main_frame = parent
        self.images_path = self.main_frame.images_path

        # Set the application icon, unsupported on Mac OS X.
        if platform.system() != 'Darwin':
            ico = wx.Icon(self.images_path + os.sep + 'icon.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)

        # Adjust window title and bitmap.
        bitmap_sizer = self.HeaderStaticText.GetContainingSizer()
        if dialog_type == 'warning':
            self.SetLabel('Warning')
            self.ErrorWarningIcon = \
                wx.StaticBitmap(self, wx.ID_ANY,
                                wx.Bitmap(self.images_path + os.sep + 'exclamation_24.png', wx.BITMAP_TYPE_ANY),
                                wx.DefaultPosition, wx.DefaultSize, 0)
            bitmap_sizer.Prepend(self.ErrorWarningIcon, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP | wx.BOTTOM, 5)
        elif dialog_type == 'error':
            self.SetLabel('Error')
            self.ErrorWarningIcon =\
                wx.StaticBitmap(self, wx.ID_ANY,
                                wx.Bitmap(self.images_path + os.sep + 'cross_24.png', wx.BITMAP_TYPE_ANY),
                                wx.DefaultPosition, wx.DefaultSize, 0)
            bitmap_sizer.Prepend(self.ErrorWarningIcon, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP | wx.BOTTOM, 5)

        # Adjust dialog header.
        if dialog_type == 'warning':
            self.HeaderStaticText.SetLabel('Warning')
        elif dialog_type == 'error':
            self.HeaderStaticText.SetLabel('Error')

        # Feed text to the multi line text control.
        if text:
            self.LogTextCtrl.SetValue(text)

    def on_window_close(self, event):
        logger.debug('Closing ErrorWarningDialog (event "%s", Id "%i").' % (event.GetClassName(), event.GetId()))
        self.Destroy()
