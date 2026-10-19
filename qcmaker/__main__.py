from audioplayer import AudioPlayer
from utils import graphics
from utils import qcm

import rich
import string
import random

def main():
    filename = ask_for_file()

    questions = qcm.build_questionnaire(filename)
    random.shuffle(questions)

    ALPHABET = string.ascii_letters
    AudioPlayer("assets/music.mp3").play(loop=True) # Audio not working

    for question in questions:
        title = question[0]

        responses = question[1]
        random.shuffle(responses)

        graphics.clear()
        graphics.show(graphics.card(title))

        i = 1
        for letter, response in zip(ALPHABET, responses):
            title = response[0]

            graphics.show(
                graphics.color("gold1") +
                graphics.text(f"({letter})") +
                graphics.text(f" {title}")
            )

            i += 1
        
        answer = input("\nSelect your answer: ")

def ask_for_file():
    response = None
    warn_msg = ""

    while True:
        graphics.clear()
        graphics.show(graphics.card("QCMAKER"))

        if warn_msg != "":
            graphics.show(graphics.warning(warn_msg))
        
        response = input("Write the directory of your questionnaire text file: ")
        try:
            open(response)
            break
        except FileNotFoundError:
            warn_msg = "Could not find text file."
    
    return response

if __name__ == "__main__":
    main()