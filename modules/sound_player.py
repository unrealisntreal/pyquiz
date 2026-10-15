import playsound3

music = None

def start_music():
    music = playsound3.playsound("assets/music.mp3", False)

def stop_music():
    music.stop()
    music = None