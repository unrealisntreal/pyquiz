from audioplayer import AudioPlayer
from utils import graphics
from utils import qcm

import rich
import string
import random

def choose_mode():
    """Demande le mode de jeu et le barème de notation."""
    while True:
        graphics.clear()
        graphics.show(graphics.card("QCMAKER"))

        print("\nChoisissez votre mode de jeu :")
        print("(1) Examen : notation avec malus")
        print("(2) Friendly : choix avec ou sans malus")

        mode = input("Votre choix (1/2) : ").strip()

        if mode == "1":
            return "Examen", "malus"

        elif mode == "2":
            while True:
                print("\nChoisissez votre notation :")
                print("(1) Avec malus")
                print("(2) Sans malus")

                notation = input("Votre choix : ").strip()

                if notation == "1":
                    return "Friendly", "malus"
                elif notation == "2":
                    return "Friendly", "sans_malus"

                print("Choix invalide. Entrez 1 ou 2.")

        print("Choix invalide. Entrez 1 ou 2.")

def score_question(responses, selected, notation):
    score = 0

    for i in range(len(responses)):
        if i in selected:
            if responses[i][1]:
                score += 1
            elif notation == "malus":
                score -= 1

    return score

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