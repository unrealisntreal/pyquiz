from textual.app import App, ComposeResult
from textual.widgets import Button


class QCMaker(App):
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [("ctrl+c", "quit", "Quit"), ("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Button("New", variant="primary")
        yield Button("Search", variant="primary")
        yield Button("Stats", variant="primary")


if __name__ == "__main__":
    app = QCMaker()
    app.run()
