from utils.quiz import Quiz, Score


def get_gamemode() -> str:
    while True:
        print("Choose your gamemode")
        print("Ranked: Score increases with reaction time.")
        print("Casual: Best fit for starters.")

        mode = input("Your pick: ").strip().lower()

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
        except:
            print("Unknown Error.")


def main():
    gamemode = get_gamemode()
    score = Score()
    quiz = get_quiz()

    for question in quiz.questions:
        print(question.get("text"))
        choices = question.get("choices")

        for position, choice in enumerate(choices):
            print(f"({position + 1}) {choice.get("text")}")

        score.register(choices, get_answers())

    print(
        f"Gamemode: {gamemode.capitalize()}\nFinal Score: {score.score}\nWith Negative Marking: {score.score - score.wrong}"
    )


if __name__ == "__main__":
    main()
