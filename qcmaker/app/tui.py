import webbrowser
import ascii

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Horizontal, Vertical, Container


class Application(App):
    TITLE = "PyQuiz"
    CSS_PATH = "style.tcss"
    ENABLE_COMMAND_PALETTE = False

    def compose(self) -> ComposeResult:
        with Container():
            with Vertical():
                yield Static(ascii.BANNER)
                yield Static(ascii.LIBRARY, classes="art")

                with Horizontal():
                    yield Button(
                        "Begin",
                        tooltip="Start a quiz!",
                    )
                    yield Button("Quit", id="quit", tooltip="Leaving already?")
                    yield Button(
                        "Github",
                        id="github",
                        tooltip="Open the github repository page",
                    )

    @on(Button.Pressed, "#quit")
    def close_app(self):
        self.exit()

    @on(Button.Pressed, "#github")
    def open_github(self):
        webbrowser.open("https://github.com/unrealisntreal/qcmaker")


if __name__ == "__main__":
    app = Application()
    app.run()
