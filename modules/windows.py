# windows
#
# Dependencies:
#   ctypes
#   win32gui
#
# Keys: 
#   {window_title}          The title of the active window

import ctypes
import win32gui
import vrcosc

def format(text):
    hwnd = win32gui.GetForegroundWindow()

    return vrcosc.str_replace_bulk(text, {
        "window_title": win32gui.GetWindowText(hwnd)
    })
