from utils import graphics
from utils import qcm

def main():
    filename = ask()

def ask():
    warn = ""

    while True:
        graphics.clear()
        graphics.show(graphics.title("QCMAKER"))

        if warn != "":
            graphics.show(graphics.warning(warn))
        
        response = input("Write the directory of your questionnaire text file: ")
        try:
            open(response)
            break
        except FileNotFoundError:
            warn = "Could not find text file."


if __name__ == "__main__":
    main()