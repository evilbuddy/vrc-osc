# hyprland
#
# Dependencies:
#   hyprpy
#
# Keys: 
#   {window_title}          The title of the active window
#   {window_initial_title}  The initial title of the active window
#   {window_class}          The class of the active window
#   
#   {workspace_id}          The ID of the active workspace
#   {workspace_name}        The name of the active workspace
#   {workspace_windows}     The number of windows in the active workspace

from hyprpy import Hyprland
import vrcosc

def init():
    global instance
    instance = Hyprland()

def format(text):
    window = instance.get_active_window()
    workspace = instance.get_active_workspace()

    return vrcosc.str_replace_bulk(text, {
        "window_title": window.title,
        "window_initial_title": window.initial_title,
        "window_class": window.wm_class,

        "workspace_id": workspace.id,
        "workspace_name": workspace.name,
        "workspace_windows": workspace.window_count
    })
