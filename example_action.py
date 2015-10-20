# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import time


def wait_some_time(queue_to_gui, queue_from_gui, file_path_list):
    for file_path in file_path_list:
        print file_path

    # Set the gauge to 25%. Status percentage must be passed as a string.
    queue_to_gui.put('25', False)
    time.sleep(2)

    # Check if user clicked cancel in the meantime. Exit function if so. Continue otherwise.
    if not queue_from_gui.empty():
        if queue_from_gui.get() == u'Cancel':
            print 'clicked cancel'
            return

    print 'not clicked cancel yet'
    queue_to_gui.put('50', False)
    time.sleep(2)

    # Check if user clicked cancel in the meantime. Exit function if so. Continue otherwise.
    if not queue_from_gui.empty():
        if queue_from_gui.get() == u'Cancel':
            print 'clicked cancel'
            return

    print 'not clicked cancel yet'
    queue_to_gui.put('75', False)
    time.sleep(2)
    queue_to_gui.put('Continuing ...', False)
    time.sleep(2)

    queue_to_gui.put('100', False)
    time.sleep(0.5)

    # Cancel because an error occurred.
    # queue_to_gui.put(u'Error: Some sample error text.', False)

    # Exit successfully.
    queue_to_gui.put(u'Finish', False)
    return
