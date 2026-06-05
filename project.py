"""Entry point for the Meaning of Life Hangman Adventure."""

import os
import time

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pyfiglet
from pygame import mixer

from game_logic import extra_life_q, hangman, innkeeper_dialogue, tea
from story_data import RULES
from utils import clear_screen, text_delay


def main():
    clear_screen()
    innkeeper_dialogue()
    game_start()
    hangman()


def game_start():
    """Introduce the hangman game with sound effects and rules."""
    mixer.init()
    mixer.music.load("drumroll.mp3")
    mixer.music.play()

    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    time.sleep(1)
    mixer.music.stop()
    clear_screen()

    mixer.music.load("partyblower.mp3")
    mixer.music.play()

    print("\n", pyfiglet.figlet_format("Hangman", font="banner3-D"))
    time.sleep(1)
    text_delay("Rules are pretty simple. Take a second to read them.\n")

    for rule in RULES:
        time.sleep(1)
        text_delay(rule)

    time.sleep(3)
    text_delay("Okay lets begin")
    time.sleep(2)
    clear_screen()


if __name__ == "__main__":
    main()
