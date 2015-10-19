# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import frame_main_gui
import dialog_errorwarning
import example_action

import logging
import logging.config
import os
import platform
import sys
import Queue
import threading

import wx
import wx.animate


# Logging config on sub-module level.
logger = logging.getLogger(__name__)


class FileDragAndDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    # The following line is marked as "signature does not match" in the IDE but it works ...
    def OnDropFiles(self, x, y, file_paths):
        self.window.launch_action(file_paths)


class FrameMain(frame_main_gui.FrameMain):
    def __init__(self, parent):
        frame_main_gui.FrameMain.__init__(self, parent)

        # Setup queuing (necessary to get something returned from a separate thread).
        self.status_queue = Queue.Queue()
        self.continue_time_refresh = True

        # Bind the "on close" event.
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Bind the browse button either to a file dialog or to a directory dialog.
        self.BrowseButton.Bind(wx.EVT_BUTTON, self.browse_for_files)
        # self.BrowseButton.Bind(wx.EVT_BUTTON, self.browse_for_folder)

        # Determine if the program is running frozen to an *.exe/*.app or from the Python interpreter.
        if hasattr(sys, 'frozen'):
            self.application_path = os.path.dirname(sys.executable)
        else:
            self.application_path = os.path.dirname(__file__)
        self.images_path = self.application_path + os.sep + 'images'

        # Set the application icon (unsupported on Mac OS X).
        if platform.system() != 'Darwin':
            ico = wx.Icon(self.images_path + os.sep + 'icon.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)

        # Adjust the background color of the static text widgets by manually specifying a color code in hex.
        # self.background_color = '#e2e2e2'  # for background.png
        self.background_color = '#ffffff'  # for background_alternative.png
        # Transparent background is not supported out of the box for static text but can be achieved:
        #  http://www.keacher.com/994/transparent-static-text-in-wxpython/
        #  http://stackoverflow.com/questions/2179173/wxpython-statictext-on-transparent-background
        self.DropHereStaticText.SetBackgroundColour(self.background_color)
        self.OrBrowseStaticText.SetBackgroundColour(self.background_color)
        self.ProgressStaticText.SetBackgroundColour(self.background_color)
        self.WaitStaticText.SetBackgroundColour(self.background_color)

        # Set the window title.
        self.SetTitle('WxPythonDragDropTemplate')

        # Add the logo image (146px x 65px).
        panel_sizer = self.DropHereStaticText.GetContainingSizer()
        logo_image = wx.Image(self.images_path + os.sep + 'logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        logo_bitmap = wx.StaticBitmap(self.DragDropPanel, wx.ID_ANY, logo_image, wx.DefaultPosition, wx.Size(146, 65))
        logo_bitmap.SetBackgroundColour(self.background_color)
        panel_sizer.Insert(1, logo_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Make the panel accept dropped objects.
        file_drop_target = FileDragAndDrop(self)
        self.DragDropPanel.SetDropTarget(file_drop_target)

        # Start the gif animation.
        self.gui_add_gif_animation()

    def gui_update(self):
        try:
            self.Update()
            self.Refresh()
            self.Layout()
            self.Freeze()
            self.Thaw()
            return True
        except Exception as err:
            logger.error('WxPython error: %s.' % err)
            return False

    def gui_panel_background(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        # background_image = wx.Bitmap(self.images_path + os.sep + 'background.png')
        background_image = wx.Bitmap(self.images_path + os.sep + 'background_alternative.png')
        dc.DrawBitmap(background_image, 0, 0)

    def gui_add_gif_animation(self):
        gif_sizer = self.WaitStaticText.GetContainingSizer()
        ani = wx.animate.Animation(self.images_path + os.sep + 'spinner.gif')
        ctrl = wx.animate.AnimationCtrl(self.ProgressGifPanel, -1, ani)
        ctrl.SetBackgroundColour(self.background_color)
        ctrl.Play()
        gif_sizer.Insert(1, ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 5)

    def browse_for_files(self, event):
        logger.debug('Frame: Browse for files (event "%s", id %i).' % (event.GetClassName(), event.GetId()))
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
            self.launch_action(selected_file_paths)

    def browse_for_folder(self, event):
        logger.debug('Frame: Browse for folder (event "%s", id %i).' % (event.GetClassName(), event.GetId()))
        choose_folder_dialog = wx.DirDialog(self, 'Choose a directory',
                                            style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR)

        if choose_folder_dialog.ShowModal() == wx.ID_OK:
            selected_file_path = choose_folder_dialog.GetPath()
            self.launch_action(selected_file_path)

    def launch_action(self, path_or_paths):
        # Check if one single path (dir picker) or a list of paths (file picker) were passed.
        paths = []
        if isinstance(path_or_paths, basestring):
            paths.append(path_or_paths)
        elif isinstance(path_or_paths, list):
            paths = path_or_paths

        # Switch from drag & drop target panel to progress indicator panel.
        # self.switch_to_progress_panel('gauge')
        self.switch_to_progress_panel('gif-spinner')

        # Launch the function that refreshes the status as well as the actual function that processes the files.
        thread_0 = threading.Thread(target=self.execute_threaded_function, name='launcher',
                                    args=(example_action.wait_some_time, paths))
        thread_0.daemon = False
        thread_0.start()

    def execute_threaded_function(self, function_to_call, objects_to_process):
        # Bind the window close event to cancel action function.
        self.Bind(wx.EVT_CLOSE, self.cancel_action)

        # Function to refresh the status.
        thread_1 = threading.Thread(target=self.refresh_status, name='status', args=())
        thread_1.daemon = True
        thread_1.start()

        # Function to process the files / folder.
        thread_2 = threading.Thread(target=function_to_call, name='function',
                                    args=(self.status_queue, objects_to_process))
        thread_2.daemon = False
        thread_2.start()

        # Continue once thread_2 (the actual function) finishes.
        thread_2.join()

        # Bind the window close event to actually closing the window again.
        self.Bind(event=wx.EVT_CLOSE, handler=self.on_close)

        # Switch from progress indicator panel back to drag & drop target panel.
        self.switch_to_drag_drop_panel()

    def switch_to_progress_panel(self, type_of_progress_panel='gauge'):
        logger.debug('Frame: Showing progress panel.')

        if type_of_progress_panel == 'gauge':
            self.DragDropPanel.Hide()
            self.ProgressGaugePanel.Show()
            self.ProgressGauge.Pulse()
        elif type_of_progress_panel == 'gif-spinner':
            self.DragDropPanel.Hide()
            self.ProgressGifPanel.Show()
            self.gui_update()

    def switch_to_drag_drop_panel(self):
        logger.debug('Frame: Showing drag & drop panel.')
        self.ProgressGaugePanel.Hide()
        self.ProgressGifPanel.Hide()
        self.DragDropPanel.Show()

    def refresh_status(self):
        while True:
            try:
                # Store queue content in variable since reading an item from the queue also removes it from the queue.
                current_message = self.status_queue.get()

                # Exit the loop as soon as a 'Finish', 'Cancel' or 'Error' message is found in queue.
                if current_message == u'Finish':
                    logger.info(u'Finished without error.')
                    break
                elif current_message == u'Cancel':
                    logger.info(u'User clicked window close while running action.')
                    # TODO
                    break
                elif current_message[:5] == u'Error':
                    if len(current_message) > 6:
                        error_text = current_message[7:]
                    else:
                        error_text = u'Unknown error occurred.'
                    logger.error(error_text)
                    dialog_errorwarning.ErrorWarningDialog(parent=self, dialog_type='error', text=error_text)\
                        .ShowModal()
                    break
                elif current_message.isdigit():
                    self.ProgressGauge.SetValue(int(current_message))

            except Exception as err:  # PyDeadObjectError may appear when thread finishes.
                logger.error(u'Exception: %s.' % err)

    def cancel_action(self, event):
        logger.debug('Frame: Cancel (event "%s", id %i).' % (event.GetClassName(), event.GetId()))
        self.status_queue.put(u'Cancel', False)

    def on_close(self, event):
        logger.debug('Frame: Close (event "%s", id %i).' % (event.GetClassName(), event.GetId()))
        self.Destroy()
