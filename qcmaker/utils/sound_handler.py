from typing import Literal
from audioplayer import AudioPlayer

type Available = Literal[
    "fail",
    "music",
    "finish"
]

audio_players = {
    "fail": AudioPlayer("assets/fail.wav"),
    "music": AudioPlayer("assets/music.wav"),
    "finish": AudioPlayer("assets/finish.wav")
}

def play(name: Available):
    if name in audio_players:
        match name:
            case "music":
                audio_players[name].play(
                    loop=True,
                    block=False
                )

            case _:
                audio_players["music"].stop()
                audio_players[name].play()

def stop(name: Available):
    if name in audio_players:
        audio_players[name].stop()