import playsound3
from playsound3.playsound3 import Sound

_music = None

def start_music():
    global _music
    _music = playsound3.playsound("assets/music.mp3", False)

def stop_music():
    global _music

    _music.stop()
    _music = None
    