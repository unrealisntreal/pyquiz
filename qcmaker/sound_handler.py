"""
    Description
    -----------
    Handles the audio heard throughout the program, powered by the `audioplayer` package.

    - Stores AudioPlayers in the Dictionary `audio_players` by getting the current working directory
      and finding the neighbour .wav files
    
    - Defines the literal type `Available` which is used throughout the different module functions
      to typehint what sounds are available in the sound library.
    
    - Defines two self-explanatory functions, `play` and `stop`, that handle when a sound should
      be heard.
"""

from utils import relative
from typing import Literal
from audioplayer import AudioPlayer

ASSET_DIR = "qcmaker/assets/"

type Available = Literal[
    "fail",
    "music",
    "finish"
]

audio_players = {
    "fail": AudioPlayer(ASSET_DIR + "fail.wav"),
    "music": AudioPlayer(ASSET_DIR + "music.wav"),
    "finish": AudioPlayer(ASSET_DIR + "finish.wav")
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