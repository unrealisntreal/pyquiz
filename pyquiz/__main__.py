import webbrowser

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Input, Rule, Static

from quiz import Quiz, Score

LOGO = """
[cornflowerblue]╭─╮[/][gold]╷ ╷[/]╭─╮╷ ╷╷╶─╮
[cornflowerblue]├─╯[/][gold]╰┬╯[/]│╮││ ││╭─╯
[cornflowerblue]╵  [/][gold] ╵ [/]╰┴╯╰─╯╵╰─╴ [grey]v0.0.1[/]
""".strip()


class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        with Vertical():
            logo = Static()
            logo.content = LOGO
            yield logo

            with Horizontal(id="mainmenu-row"):
                begin_button = Button()
                begin_button.id = "begin"
                begin_button.label = "Begin"
                yield begin_button

                quit_button = Button()
                quit_button.id = "quit"
                quit_button.label = "Quit"
                yield quit_button

                github_button = Button()
                github_button.id = "github"
                github_button.label = "Github"
                yield github_button

    @on(Button.Pressed, "#begin")
    def begin_quiz(self):
        self.app.switch_screen(SetupScreen())

    @on(Button.Pressed, "#quit")
    def quit_app(self):
        self.app.exit()

    @on(Button.Pressed, "#github")
    def open_github(self):
        webbrowser.open("https://github.com/unrealisntreal/qcmaker")


class SetupScreen(Screen):
    def compose(self) -> ComposeResult:
        with Vertical():
            negative_marking = Button()
            negative_marking.id = "negative-marking"
            negative_marking.label = "[red](OFF)[/] Negative Marking"
            yield negative_marking

            path_input = Input()
            path_input.id = "path-input"
            path_input.placeholder = "Insert the quiz path here..."
            yield path_input

            with Horizontal():
                confirm_button = Button()
                confirm_button.id = "confirm"
                confirm_button.label = "Confirm"
                yield confirm_button

                go_back_button = Button()
                go_back_button.id = "go-back"
                go_back_button.label = "Go Back"
                yield go_back_button

    @on(Button.Pressed, "#negative-marking")
    def enable_negative_marking(self):
        negative_marking_button = self.query_one("#negative-marking", Button)
        negative_marking_text   = str(negative_marking_button.label)
        negative_marking        = "ON" in negative_marking_text

        if negative_marking:
            negative_marking_button.label = "[red](OFF)[/] Negative Marking"
        else:
            negative_marking_button.label = "[green](ON)[/] Negative Marking"

    @on(Button.Pressed, "#confirm")
    def confirm(self):
        try:
            path = self.query_one("#path-input", Input).value
            quiz = Quiz(path)

            negative_marking_button = self.query_one("#negative-marking", Button)
            negative_marking_text   = str(negative_marking_button.label)
            negative_marking        = "ON" in negative_marking_text

            quiz_screen = QuizScreen(
                quiz=quiz,
                score=Score(),
                negative_marking=negative_marking,
                current=0
            )

            self.app.notify("Found Quiz!")
            self.app.switch_screen(quiz_screen)
        except Exception as e:
            self.app.notify(
                title=type(e).__name__,
                message=str(e),
                severity="error"
            )

    @on(Button.Pressed, "#go-back")
    def go_back(self):
        self.app.switch_screen(MainMenuScreen())


class QuizScreen(Screen):
    def __init__(self, quiz: Quiz, score: Score, negative_marking: bool, current: int):
        super().__init__()
        self.quiz = quiz
        self.score = score
        self.qname = quiz.name
        self.qauthor = quiz.author
        self.questions = quiz.questions
        self.negative_marking = negative_marking

        self.current = current

    def compose(self) -> ComposeResult:
        question = self.questions[self.current]
        choices  = question.get("choices")

        with Vertical():
            static_name = Static()
            static_name.content = "[grey][bold]" + self.qname
            yield static_name

            static_author = Static()
            static_author.content = "[grey]" + self.qauthor
            yield static_author

            yield Rule()

            static_question = Static()
            static_question.content = question.get("text")
            yield static_question

            for position, choice in enumerate(choices):
                static_choice = Static()
                static_choice.content = f"[gold]({position + 1})[/] " + choice.get("text")
                yield static_choice

            yield Rule()

            answer_input = Input()
            answer_input.id = "answer-input"
            answer_input.placeholder = "Select your answer(s) here... (ex: 1, 3)"
            yield answer_input

            confirm_button = Button()
            confirm_button.id = "confirm"
            confirm_button.label = "Confirm"
            yield confirm_button

    @on(Button.Pressed, "#confirm")
    def confirm(self):
        question = self.questions[self.current]
        choices  = question.get("choices")

        try:
            response = self.query_one("#answer-input", Input).value
            response = response.strip().split(",")

            answers = []
            for c in response:
                try:
                    answer = int(c.strip())
                except ValueError:
                    raise ValueError("Answer is not formatted correctly.")

                if answer < 1 or answer > len(choices):
                    raise ValueError("Answer is out of bounds.")
                answers.append(answer)
        except ValueError as e:
            self.app.notify(
                title="Error",
                message=str(e),
                severity="error"
            )
            return

        is_correct, feedbacks = self.score.register(choices, answers)

        feedbacks_str = ""
        if feedbacks:
            for feedback in feedbacks:
                feedbacks_str += f"\n- {feedback}"

        if is_correct:
            self.app.notify(
                title="Correct :)",
                message=feedbacks_str,
                severity="information"
            )
        else:
            self.app.notify(
                title="Incorrect :(",
                message=feedbacks_str,
                severity="error"
            )

        nxt = self.current + 1
        if nxt == len(self.questions):
            if self.negative_marking:
                message = f"""
                Score: {self.score.score}
                """
            else:
                message = f"""
                Score: {self.score.score - self.score.wrong}
                """

            self.app.switch_screen(MainMenuScreen())
            self.app.notify(
                title="Finished!",
                message=message,
                severity="information"
            )
            return

        quiz_screen = QuizScreen(
            quiz=self.quiz,
            score=self.score,
            negative_marking=self.negative_marking,
            current=nxt
        )
        self.app.switch_screen(quiz_screen)



class Application(App):
    TITLE = "PyQuiz"
    CSS_PATH = "style.tcss"
    NOTIFICATION_TIMEOUT = 5.0
    ENABLE_COMMAND_PALETTE = False

    def on_mount(self):
        self.push_screen(MainMenuScreen())


if __name__ == "__main__":
    app = Application()
    app.run()
