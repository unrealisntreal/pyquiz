import json
import random

DEFAULT_NAME = "Untitled Quiz"
DEFAULT_AUTHOR = "Unknown Author"


def decode_legacy(path: str) -> list:
    """Legacy solution to decode quiz configuration files."""

    questions = []
    wording = None
    choices = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if "|" not in line:
                if wording or choices:
                    questions.append([wording, choices])
                wording = None
                choices = []
            else:
                parts = line.strip().split("|")
                if 1 < len(parts) < 5:
                    if parts[0] == "Q":
                        if not wording and not choices:
                            wording = parts[1]
                            choices = []
                        else:
                            questions.append([wording, choices])
                            wording = None
                            choices = []
                    elif parts[0] == "A":
                        if parts[2] not in ("V", "X"):
                            print(f"Error when loading line:\n\t{line}")
                        else:
                            choices.append(
                                [
                                    parts[1],
                                    parts[2] == "V",
                                    parts[3] if len(parts) > 3 else "",
                                ]
                            )
                    else:
                        print(f"Error when loading line:\n\t{line}")
                else:
                    print(f"Error when loading line:\n\t{line}")

                if line.startswith("Q"):
                    wording = parts[1]

    if wording or choices:
        questions.append([wording, choices])
    return questions


class Quiz:
    name: str
    author: str
    questions: list

    def __init__(self, path: str):
        if path.endswith(".txt"):
            try:
                with open(path, mode="r", encoding="utf-8") as file:
                    legacy_questions = decode_legacy(path)
            except:
                raise ValueError("Unknown Legacy Decoding Error.")

            questions = []
            for i, legacy_question in enumerate(legacy_questions):
                choices = []
                for legacy_choice in legacy_question[1]:
                    choices.append(
                        {
                            "text": legacy_choice[0],
                            "correct": legacy_choice[1],
                            "feedback": legacy_choice[2],
                        }
                    )
                questions.append({"text": legacy_question[0], "choices": choices})

            self.name = DEFAULT_NAME
            self.author = DEFAULT_AUTHOR
            self.questions = questions

        elif path.endswith(".json"):
            try:
                with open(path, mode="r", encoding="utf-8") as file:
                    quiz = json.load(file)
            except FileNotFoundError:
                raise FileNotFoundError(f"Quiz could not be found in path {path}")
            except json.JSONDecodeError:
                raise ValueError("Quiz contains invalid JSON code.")

            if not isinstance(quiz, dict):
                raise TypeError("Quiz JSON root must be a dictionary.")

            questions = quiz.get("questions")
            if not questions:
                raise ValueError("Quiz does not have any questions.")

            for i, question in enumerate(questions):
                choices = question.get("choices")
                if not choices:
                    raise ValueError(f"Question {i} does not have any choices.")

            self.name = quiz.get("name", DEFAULT_NAME)
            self.author = quiz.get("author", DEFAULT_AUTHOR)
            self.questions = questions

        self.shuffle()

    def shuffle(self):
        """Randomizes the position of questions and choices within the quiz."""

        questions = self.questions
        random.shuffle(questions)

        for question in questions:
            choices = question.get("choices")
            random.shuffle(choices)


class Score:
    def __init__(self):
        self.score = 0
        self.wrong = 0

    def register(self, choices: list, answers: list) -> tuple[bool, list]:
        """
        Updates the score with the user's answers for a question.

        Args:
            choices: The list of options available for the question.
            answers: The list of answers chosen by the user.

        Returns:
            bool: Represents if the answers were correct.
            list: Feedback message for each answer.
        """

        correct = True
        feedbacks = []

        if not answers:
            correct = False
        else:
            for answer in answers:
                if answer < 1 or answer > len(choices):
                    correct = False
                    break

            if correct == True:
                for i, choice in enumerate(choices):
                    is_selected = (i + 1) in answers
                    is_correct  = choice.get("correct", False)
                    is_required = choice.get("required", False)

                    if is_selected:
                        feedback = choice.get("feedback")
                        if feedback:
                            feedbacks.append(feedback)

                    if (is_selected and not is_correct) or (not is_selected and is_required):
                        correct = False
                        break

        if correct:
            self.score += 1
        else:
            self.wrong += 1

        return correct, feedbacks
