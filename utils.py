"""Small utility functions used across the game."""

import os
import time


def clear_screen():
    """Clear the terminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def text_delay(anim_text):
    """Print text one character at a time to create a dialogue effect."""
    for character in anim_text:
        print(character, end="", flush=True)
        time.sleep(0.03)
    print()
    return "text has been animated"
