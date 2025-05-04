# mac
#
# Keys: 
#   {window_class}          The name of the current application
#   {window_title}          Ditto.

# I don't know anything about applescript, sorry.

import subprocess
import vrcosc

def format(text):
    script = '''
tell application "System Events"
    set frontApp to name of first application process whose frontmost is true
end tell
return frontApp
'''

    app_name = subprocess.check_output(['osascript', '-e', script]).strip()
    return vrcosc.str_replace_bulk(text, {
        "window_class": app_name.decode(),
        "window_title": app_name.decode()
    })
