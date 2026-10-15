"""
    Description
    -----------
    Module permettant d'afficher des visuels complexes pour applications de terminal.

    - Génère des visuels avec les fonctions `separator`, `center`, `warning`, ...
    - Affiche les visuels avec la commande `show`.
"""

import os
import rich

def show(text: str):
    rich.print(text)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def warning(text: str) -> str:
    return r"[gold1]/!\ " + text

def separator(length: int, color: str) -> str:
    return f"[{color}]{"=" * length}[/{color}]"

def center(text: str, length: int = 1, color: str = "white") -> str:
    return f"[{color}]{text.center(length)}[/{color}]"

def rainbow_seperator(length: int) -> str:
    colors = [
        "red", "dark_orange", "gold1",
        "green", "blue", "hot_pink",
        "purple"
    ]

    text = ""

    i = 0
    j = 0
    while i < length:
        if j == len(colors):
            j = 0
        color = colors[j]

        text += separator(length=1, color=color)
        i += 1
        j += 1
    
    return text

def title(text: str):
    length = 50

    return f"""
    {rainbow_seperator(length=length)}
    {center(text=text, length=length, color="gold1")}
    {rainbow_seperator(length=length)}
    """