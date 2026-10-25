import webbrowser
from app import ascii

from textual import on, events
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
                static_banner = Static()
                static_banner.content = ascii.BANNER
                yield static_banner

                icon_banner = Static()
                icon_banner.id = "icon-banner"
                icon_banner.content = ascii.BOOK
                icon_banner.classes = "art"
                yield icon_banner

                with Horizontal(id="mainmenu-row"):
                    begin_button = Button()
                    begin_button.id = "begin"
                    begin_button.label = "Begin"
                    begin_button.tooltip = "Start a quiz!"
                    yield begin_button

                    quit_button = Button()
                    quit_button.id = "quit"
                    quit_button.label = "Quit"
                    quit_button.tooltip = "Leaving already?"
                    yield quit_button

                    github_button = Button()
                    github_button.id = "github"
                    github_button.label = "Github"
                    github_button.tooltip = "Open the github repository page"
                    yield github_button

    @on(events.Enter, "#begin")
    def on_begin_enter(self):
        self.query_one("#icon-banner", Static).content = ascii.BOOK

    @on(Button.Pressed, "#quit")
    def quit_app(self):
        self.exit()

    @on(events.Enter, "#quit")
    def on_quit_enter(self):
        self.query_one("#icon-banner", Static).content = ascii.EXIT

    @on(Button.Pressed, "#github")
    def open_github(self):
        webbrowser.open("https://github.com/unrealisntreal/qcmaker")

    @on(events.Enter, "#github")
    def on_github_enter(self):
        self.query_one("#icon-banner", Static).content = ascii.GITHUB
