from typing import Literal

import string
import random

type Responses = list[list[str, bool]]
type Gamemode = Literal["ranked", "casual"]
type Answers = list[str]

class Score:
    def __init__(self):
        self.score: float = 0.0
        self.wrong: float = 0.0
    
    def register(self, responses: Responses, answers: Answers):
        correct = True
        for response, answer in zip(responses, answers):
            if answer == response[0]:
                if not response[1]:
                    correct = False
                    self.wrong += 1
    
        if correct:
            self.score += 1
    
    def __str__(self):
        return f"""
        Final Score:
        No malus: {score}
        Malus: {score - wrong}
        """

def get_gamemode() -> Gamemode:
    while True:
        print("\nChoose your gamemode :")
        print("Ranked : seul le score avec malus est affiché")
        print("Casual : score sans malus, et score avec malus si vous le demandez")

        mode = input("Your pick : ").strip().lower()

        if mode is Gamemode:
            return mode
        else:
            print("Invalid choice.")

def get_answers(responses: list) -> Answers:
    while True:
        answers = input("Choose your answers : ").strip().lower()

        try:
            l = list(answers)
            return answers
        except:
            print("Invalid formatting.")

def get_file() -> any:
    while True:
        response = input("Write the directory of your questionnaire text file: ")
        
        try:
            file = open(response)
            file.close()
            break
        except PermissionError:
            print("Could not get permission to open file.")
        except FileNotFoundError:
            print("Could not find text file.")
    
    return response

def main():
    ALPHABET = string.ascii_lowercase

    filename = get_file()
    gamemode = get_gamemode()
    score    = Score()

    questions = qcm.build_questionnaire(filename)
    random.shuffle(questions)

    for question in questions:
        print(question[0])

        responses = question[1]
        random.shuffle(responses)

        for letter, response in zip(ALPHABET, responses):
            print(f"({letter}) {response[0]}")

        answers = get_answers()

        total_sans_malus += score_question(responses, selected, "sans_malus")  
        total_avec_malus += score_question(responses, selected, "malus")

    print(gamemode)
    print(score)

if __name__ == "__main__":
    main()