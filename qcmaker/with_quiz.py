from typing import Literal
from utils.quiz import Quiz, Score

import random

def get_gamemode() -> str:
    while True:
        print("Choose your gamemode")
        print("Ranked : seul le score avec malus est affiché")
        print("Casual : score sans malus, et score avec malus si vous le demandez")

        mode = input("Your pick : ").strip().lower()

        if mode in ("casual", "ranked"):
            return mode
        else:
            print("Invalid choice.")

def get_answers() -> list:
    while True:
        response = input("Choose your answers : ").strip().split(",")

        try:
            return [int(c.strip()) for c in response]
        except:
            print("Unknown Error.")

def get_quiz() -> str:
    while True:
        response = input("Write the directory of your quiz text file: ")
        
        try:
            quiz = Quiz(response)
            open(response).close()
            return response
        except any as error:
            print(error)

def show_question_title(question: list):
    print(question[0])

def main():
    filepath  = get_filepath()
    gamemode  = get_gamemode()
    questions = get_questions(filepath)
    score     = Score()

    for question in questions:
        print(question[0])
        responses = get_responses(question)

        for position, response in enumerate(responses):
            print(f"({position}) {response[0]}")
        
        score.register(responses, get_answers())

    print(gamemode)
    print(score)

if __name__ == "__main__":
    main()