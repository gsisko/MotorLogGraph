# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import gui

import os
import platform
import sys

import wx
import wx.animate


class FileDragAndDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    # The following line is marked as "signature does not match" in the IDE but it works ...
    def OnDropFiles(self, x, y, file_paths):
        self.window.do_some_action(file_paths)


class MainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

        # Bind the "on close" event.
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Bind the browse button either to a file dialog or to a directory dialog.
        self.BrowseButton.Bind(wx.EVT_BUTTON, self.browse_for_files)
        # self.BrowseButton.Bind(wx.EVT_BUTTON, self.browse_for_folder)

        # Determine if the program is running compiled to an *.exe/*.app or from the Python interpreter.
        if hasattr(sys, 'frozen'):
            self.application_path = os.path.dirname(sys.executable)
        else:
            self.application_path = os.path.dirname(__file__)

        # Set the application icon (unsupported on Mac OS X).
        if platform.system() != 'Darwin':
            ico = wx.Icon(self.application_path + os.sep + 'icon.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)

        # Set window title.
        self.SetTitle('WxPythonDragDropTemplate')

        # Add logo image (120px x 30px).
        panel_sizer = self.DropHereStaticText.GetContainingSizer()
        logo_image = wx.Image(self.application_path + os.sep + 'logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        logo_bitmap = wx.StaticBitmap(self.DragDropPanel, wx.ID_ANY, logo_image, wx.DefaultPosition, wx.Size(120, 30),
                                      0)
        panel_sizer.Insert(1, logo_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Make the panel accept drag & dropped objects.
        file_drop_target = FileDragAndDrop(self)
        self.DragDropPanel.SetDropTarget(file_drop_target)

    def add_drag_drop_panel_background(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        background_image = wx.Bitmap(self.application_path + os.sep + 'background.png')
        dc.DrawBitmap(background_image, 0, 0)

    def do_some_action(self, path_or_paths):
        # Check if one single path or a list of paths were passed.
        if isinstance(path_or_paths, basestring):
            print path_or_paths

        if isinstance(path_or_paths, list):
            for file_path in path_or_paths:
                print file_path

        # Switch from drag & drop target to progress indicator panel.
        self.switch_to_progress_panel('gif-spinner')

        # Switch from progress indicator to drag & drop target panel.
        self.switch_to_drag_drop_panel()

    def switch_to_progress_panel(self, type_of_progress_panel='gauge-undetermined'):
        if type_of_progress_panel == 'gauge-undetermined':
            self.DragDropPanel.Hide()
            self.ProgressGaugePanel.Show()
            self.ProgressGauge.Pulse()
        elif type_of_progress_panel == 'gauge-determined':
            self.DragDropPanel.Hide()
            self.ProgressGaugePanel.Show()
            self.ProgressGauge.SetValue(30)
        elif type_of_progress_panel == 'multi-gauge':
            self.DragDropPanel.Hide()
            self.ProgressMultiGaugePanel.Show()
            self.ProgressOneGauge.SetValue(40)
            self.ProgressTwoGauge.SetValue(60)
        elif type_of_progress_panel == 'gif-spinner':
            gif_sizer = self.WaitStaticText.GetContainingSizer()
            ani = wx.animate.Animation(self.application_path + os.sep + 'spinner.gif')
            ctrl = wx.animate.AnimationCtrl(self.DragDropPanel, -1, ani)
            ctrl.SetUseWindowBackgroundColour()
            ctrl.Play()
            gif_sizer.Insert(1, ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 5)
            self.DragDropPanel.Hide()
            self.ProgressGifPanel.Show()
            self.gui_update()

    def gui_update(self):
        """
        Run the usual wxPython functions to get the GUI to display what you want.

        :return Boolean: True if success, False if some exception was caught. GUI might not be updated in this case.
        """
        try:
            self.Update()
            self.Refresh()
            self.Layout()
            self.Freeze()
            self.Thaw()
            return True
        except Exception as err:
            return False

    def switch_to_drag_drop_panel(self):
        self.ProgressGaugePanel.Hide()
        self.ProgressMultiGaugePanel.Hide()
        self.ProgressGifPanel.Hide()
        self.DragDropPanel.Show()

    def browse_for_files(self, event):
        file_wildcards = 'Python source (*.py)|*.py|' \
                         'Compiled Python (*.pyc)|*.pyc|' \
                         'SPAM files (*.spam)|*.spam|'    \
                         'Egg file (*.egg)|*.egg|'\
                         'All files (*.*)|*.*'

        choose_file_dialog = wx.FileDialog(self, message='Choose a file', defaultDir=os.getcwd(),
                                           defaultFile='', wildcard=file_wildcards,
                                           style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)

        if choose_file_dialog.ShowModal() == wx.ID_OK:
            selected_file_paths = choose_file_dialog.GetPaths()
            self.do_some_action(selected_file_paths)

    def browse_for_folder(self, event):
        choose_folder_dialog = wx.DirDialog(self, 'Choose a directory',
                                            style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR)

        if choose_folder_dialog.ShowModal() == wx.ID_OK:
            selected_file_path = choose_folder_dialog.GetPath()
            self.do_some_action(selected_file_path)

    def on_close(self, event):
        self.Destroy()
