import graphics

from rich import print 
from rich.prompt import Prompt

def main():
    filename = ask()

def ask():
    warn = False

    while True:
        graphics.clear()
        graphics.title()

        if warn: graphics.warning("Could not find text file.")
        response = Prompt.ask("Write the directory of your questionnaire text file")
        
        warn = True
    
    return ask

if __name__ == "__main__":
    main()