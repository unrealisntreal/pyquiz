from typing import Literal
from utils import qcm

import random

# Types are wrong. Don't look. This is useless.
# It'll break if you remove them though.
type ResponseItem = list[str, bool, str]
type Responses = list[ResponseItem]
type Questions = list[str, Responses]
type Gamemode = Literal["ranked", "casual"]
type Answers = list[int]


class Score:
    def __init__(self):
        self._score: float = 0.0
        self._wrong: float = 0.0

    def register(self, responses: Responses, answers: Answers):
        if answers == []:
            return

        correct = True
        for answer in answers:
            if answer < 0 or answer >= len(responses):
                return

            if not responses[answer][1]:
                correct = False

        if correct:
            self._score += 1
        else:
            self._wrong += 1

    def __str__(self):
        return f"""
        Final Score
        No malus: {self._score}
        Malus: {self._score - self._wrong}
        """


def get_gamemode() -> Gamemode:
    while True:
        print("Choose your gamemode")
        print("Ranked : seul le score avec malus est affiché")
        print("Casual : score sans malus, et score avec malus si vous le demandez")

        mode = input("Your pick : ").strip().lower()

        if mode in ("casual", "ranked"):
            return mode
        else:
            print("Invalid choice.")


def get_answers() -> Answers:
    while True:
        response = input("Choose your answers : ").strip().split(",")

        try:
            return [int(c.strip()) for c in response]
        except:
            print("Unknown Error.")


def get_filepath() -> str:
    while True:
        response = input("Write the directory of your questionnaire text file: ")

        try:
            open(response).close()
            return response
        except PermissionError:
            print("Could not get permission to open file.")
        except FileNotFoundError:
            print("Could not find text file.")


def get_questions(filepath: str) -> list:
    questions = qcm.build_questionnaire(filepath)
    random.shuffle(questions)

    return questions


def get_responses(question: list) -> list:
    responses = question[1]
    random.shuffle(responses)

    return responses


def show_question_title(question: list):
    print(question[0])


def main():
    filepath = get_filepath()
    gamemode = get_gamemode()
    questions = get_questions(filepath)
    score = Score()

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
