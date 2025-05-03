# xorg
#
# Dependencies:
#   xlib
#
# Keys: 
#   {window_title}          The title of the active window
#   {window_class}          The class of the active window

from XLib import X, display, Xatom
import vrcosc

def init():
    global d, root
    d = display.Display()
    root = d.screen().root

def format(text):
    window = d.get_input_focus().focus

    return vrcosc.str_replace_bulk(text, {
        "window_title": window.get_wm_name(),
        "window_class": window.get_wm_class()
    })
