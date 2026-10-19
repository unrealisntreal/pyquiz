"""
    Description
    -----------
    Module permettant d'afficher des visuels complexes pour applications de terminal.

    - Génère des visuels avec les fonctions `separator`, `center`, `warning`, ...
    - Affiche les visuels avec la commande `show`.
"""

import os
import rich

_color = "white"

def show(text: str):
    rich.print(text)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def text(content: str) -> str:
    global _color
    t = f"[{_color}]{content}[/{_color}]"
    _color = "white"

    return t

def color(color: str) -> str:
    global _color
    _color = color
    return ""

def warning(content: str) -> str:
    color("gold1")
    return text("/!\ " + content)

def separator(length: int) -> str:
    return text("=" * length)

def center(content: str, length: int = 1) -> str:
    return text(content.center(length))

def rainbow_seperator(length: int) -> str:
    COLORS = (
        "red", "dark_orange", "gold1", "green",
        "blue", "hot_pink", "purple"
    )

    sep = ""

    i = 0
    j = 0
    while i < length:
        if j == len(COLORS):
            j = 0

        sep += color(COLORS[j]) + text("=")

        i += 1
        j += 1
    
    return sep

def card(text: str):
    LENGTH = 50

    return f"""
    {rainbow_seperator(LENGTH)}
    {color("gold1") + center(text, LENGTH)}
    {rainbow_seperator(LENGTH)}
    """