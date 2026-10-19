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

def color(color: str, text: str) -> str:
    return f"[{color}]{text}[/{color}]"

def warning(text: str) -> str:
    return color(
        color="gold1",
        text=r"/!\ " + text
    )

def separator(length: int) -> str:
    return "=" * length

def center(text: str, length: int = 1) -> str:
    return text.center(length)

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
        
        text += color(
            color=colors[j],
            text="="
        )
        i += 1
        j += 1
    
    return text

def card(text: str):
    length = 50

    return f"""
    {rainbow_seperator(length)}
    {color(color="gold1", text=center(text, length))}
    {rainbow_seperator(length)}
    """