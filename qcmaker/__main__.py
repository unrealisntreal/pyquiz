from utils import graphics
from utils import qcm

from rich.prompt import Prompt

def main():
    filename = ask()

def ask():
    warn = False

    while True:
        graphics.clear()
        graphics.show(graphics.title("QCMAKER"))

        if warn:
            graphics.show(graphics.warning("Could not find text file."))
        response = Prompt.ask("Write the directory of your questionnaire text file")
        
        warn = True

if __name__ == "__main__":
    main()