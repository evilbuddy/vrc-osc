# mpris
# 
# Dependencies:
#   dbus
# 
# Keys:
#   {media_player}          The name of the currently playing media player
#   {media_title}           The title of the currently playing media
#   {media_artist}          The artist of the currently playing media
#   {media_length}          The length of the currently playing media
#   {media_album}           The album of the currently playing media
#   {media_dash}            A dash character that only appears if the media player is playing

import dbus
import vrcosc

def get_main_mpris_player():
    for service in session_bus.list_names():
        if service.startswith("org.mpris.MediaPlayer2."):
            try:
                obj = session_bus.get_object(service, "/org/mpris/MediaPlayer2")
                props = dbus.Interface(obj, "org.freedesktop.DBus.Properties")
                status = props.Get("org.mpris.MediaPlayer2.Player", "PlaybackStatus")
                if status == "Playing":
                    return service
            except dbus.exceptions.DBusException:
                continue
    return None

def init():
    global session_bus
    session_bus = dbus.SessionBus()

def format(text):
    player = get_main_mpris_player()
    title = ""
    artist = ""
    album = ""
    length = 0

    if player:
        player_object = session_bus.get_object(player, "/org/mpris/MediaPlayer2")
        interface = dbus.Interface(player_object, "org.freedesktop.DBus.Properties")
        metadata = interface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        title = metadata.get("xesam:title", "Unknown")
        artist = metadata.get("xesam:artist", ["Unknown"])[0]
        album = metadata.get("xesam:album", "Unknown")
        length = round(metadata.get("mpris:length", 0) / 1000000)
    
    return vrcosc.str_replace_bulk(text, {
        "media_player": player,
        "media_title": title,
        "media_artist": artist,
        "media_length": str(length),
        "media_album": album,
        "media_dash": " - " if player else ""
    })
