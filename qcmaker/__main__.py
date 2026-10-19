from utils import graphics
from utils import qcm

import rich
import random

def main():
    filename = ask_for_file()

    questions = qcm.build_questionnaire(filename)
    random.shuffle(questions)

    for q in questions:
        print(q[0])

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