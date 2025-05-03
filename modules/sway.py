# sway
# (works with i3, sway & wayfire)
#
# Dependencies:
#   i3ipc
#
# Keys: 
#   {window_title}          The title of the active window
#   {window_class}          The class of the active window

import i3ipc
import vrcosc

def init():
    global i3
    i3 = i3ipc.connection()

def format(text):
    window = i3.get_tree().find_focused()

    return vrcosc.str_replace_bulk(text, {
        "window_title": window.name,
        "window_class": window.window_class,
    })
