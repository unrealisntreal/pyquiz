from typing import Literal
from utils.quiz import Quiz, Score

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

def get_quiz() -> Quiz:
    while True:
        response = input("Insert the directory of your quiz text file: ")
        
        try:
            quiz = Quiz(response)
            return quiz
        except any as error:
            print(error)

def show_question_title(question: list):
    print(question[0])

def main():
    gamemode = get_gamemode()
    score    = Score()
    quiz     = get_quiz()

    for question in quiz.questions:
        print(question.get("text"))
        choices = question.get("choices")

        for position, choice in enumerate(choices):
            print(f"({position + 1}) {choice.get("text")}")
        
        score.register(choices, get_answers())

    print(gamemode)
    print(f"""
    Final Score
    Sans Malus: {score.score}
    Avec Malus: {score.score - score.wrong}
    """)

if __name__ == "__main__":
    main()