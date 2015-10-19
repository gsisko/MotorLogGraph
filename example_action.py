# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import time


def wait_some_time(message_queue, file_path_list):
    for file_path in file_path_list:
        print file_path

    # Set the gauge to 25%. Status percentage must be passed as a string.
    message_queue.put('25', False)

    time.sleep(1)
    message_queue.put('50', False)
    time.sleep(1)
    message_queue.put('75', False)
    time.sleep(1)
    message_queue.put('100', False)
    time.sleep(0.5)

    # Cancel because an error occurred.
    # message_queue.put(u'Error: Some sample error text.', False)

    # Exit successfully.
    message_queue.put(u'Finish', False)
