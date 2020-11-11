import colored
from colored import stylize
from colored import fore, back, style

from datetime import datetime



# magenta
def debug(message):
    style = colored.bg("magenta") + colored.attr("bold")
    timelabel("DEBUG", style)
    print("\n\n" + message + "\n\n")

# White/Blue
def info(message):
    style = colored.bg("white") + colored.attr("bold")
    timelabel("INFO", style)
    print(message)

# Orange
def warning(message):
    style = colored.bg("orange_1") + colored.attr("bold")
    timelabel("WARNING", style)
    print(message)

# Greem
def success(message):
    style = colored.bg("green") + colored.attr("bold")
    timelabel("SUCCESS", style)
    print(message)

# red
def error(message):
    style = colored.bg("light_red") + colored.attr("bold")
    timelabel("ERROR", style)
    print(message)

# strong red
def critical(message):
    style = colored.bg("red") + colored.attr("bold")
    timelabel("!!! CRITICAL !!!", style)
    print(message)

def setup(message):
    style = colored.bg("blue_3b") + colored.attr("bold")
    timelabel("SETUP", style)
    print(message)

def timelabel(lvl, style):
    now = datetime.utcnow()
    now = now.strftime("%Y-%m-%d %H:%M")
    print(f"[{now}]", end=" ")

    maxlength = 8
    add = maxlength - len(lvl)
    spaces = ""
    for i in range(add):
        spaces = spaces + " "

    print(stylize(f"{spaces}{lvl} ", style), end=" - ")