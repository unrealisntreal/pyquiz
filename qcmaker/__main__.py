from audioplayer import AudioPlayer
from utils import graphics
from utils import qcm

import rich
import string
import random

def choose_mode():
    """Demande le mode de jeu: Examen ou fiendly"""
    warn_msg = ""
    while True:
        graphics.clear()
        graphics.show(graphics.card("QCMAKER"))

        if warn_msg != "":
            graphics.show(graphics.warning(warn_msg))

        print("\nChoisissez votre mode de jeu :")
        print("(1) Examen : seul le score avec malus est affiché")
        print("(2) Friendly : score sans malus, et score avec malus si vous le demandez")

        mode = input("Votre choix : ").strip()

        if mode == "1":
            return "Examen"
        
        elif mode == "2":
            return "Friendly"
        else:
            warn_msg = "Choix invalide. Entrez 1 ou 2."

def score_question(responses, selected, notation):
    nb_correct = 0
    for response in responses:
        if response[1]:
            nb_correct += 1
    nb_wrong = len(responses) - nb_correct

    # Pas de réponse (ou question sans bonne réponse) : 0 point
    if len(selected) == 0 or nb_correct == 0:
        return 0

    # On compte les bonnes et les mauvaises réponses cochées
    good = 0
    bad = 0
    for i in selected:
        if responses[i][1]:
            good += 1
        else:
            bad += 1

    # Choix unique
    if nb_correct == 1:
        if good == 1:
            return 1
        if notation == "malus":
            return -1
        return 0

    # Choix multiple : une question vaut 1 point maximum
    score = good / nb_correct
    if bad > 0:
        if notation == "malus":
            score -= bad / nb_wrong
        else:
            score = 0
    return score



def is_multiple(responses):
    """Renvoie True si la question a plusieurs bonnes réponses."""
    nb_correct = 0
    for response in responses:
        if response[1]:
            nb_correct += 1
    return nb_correct > 1

def main():
    filename = ask_for_file()
    mode = choose_mode()

    questions = qcm.build_questionnaire(filename)
    random.shuffle(questions)

    ALPHABET = string.ascii_letters
    AudioPlayer("assets/music.mp3").play(loop=True) #Audio marche pas
    
    total_sans_malus = 0
    total_avec_malus = 0

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
        
        multiple = is_multiple(responses) #cherche si la question a plusieurs bonnes réponses
        selected = ask_for_answer(len(responses), multiple)

        total_sans_malus += score_question(responses, selected, "sans_malus")  
        total_avec_malus += score_question(responses, selected, "malus")

    show_results(mode, len(questions), total_sans_malus, total_avec_malus)

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