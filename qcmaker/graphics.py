import os
import rich

separator_length = 50

colors = [
    "red", "dark_orange", "gold1",
    "green", "blue", "hot_pink",
    "purple"
]

def warning(text: str):
    rich.print("[gold1]/!\ " + text)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title():
    separator()
    rich.print("[gold1]" + "QCMAKER".center(separator_length) + "[/gold1]")
    separator()

def separator():
    text = ""

    i = 0
    j = 0
    while i < separator_length:
        if j == len(colors):
            j = 0
        
        color = colors[j]
        text += f"[{colors[j]}]=[/{color}]"

        i += 1
        j += 1
    
    rich.print(text)
