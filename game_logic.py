"""Core game logic for the Meaning of Life Hangman Adventure."""

import html
import random
import re
import sys
import time

import requests

from story_data import (
    HANGMAN_ASCII,
    INNKEEPER_DIALOGUE_NO,
    INNKEEPER_DIALOGUE_YES,
    LETTERS_ORIGINAL,
    MEANINGS_OF_LIFE,
    TEA_DIALOGUE,
    TEA_LIST,
)
from utils import clear_screen, text_delay


def innkeeper_dialogue():
    """Run the introductory innkeeper dialogue."""
    for index, dialogue in enumerate(INNKEEPER_DIALOGUE_YES):
        text_delay(dialogue)

        if index == len(INNKEEPER_DIALOGUE_YES) - 1:
            break

        answer = input().lower().strip()

        if index != 1:
            while answer not in ("yes", "no"):
                text_delay("It's a yes or no question dear")
                answer = input().lower().strip()

        if index == 1:
            text_delay(tea(answer))

        if index == 2:
            answer = "no" if answer == "yes" else "yes"

        if answer == "no":
            text_delay(INNKEEPER_DIALOGUE_NO[index])
            sys.exit(1)


def hangman(answer=None):
    """Run the hangman game loop."""
    if answer is None:
        answer = random.choice(MEANINGS_OF_LIFE)

    letters = LETTERS_ORIGINAL
    lives = 7
    extra_life = 0
    wrong_letters = ""

    while True:
        result = re.sub("[" + letters + "]", "_", answer)
        print(HANGMAN_ASCII[lives - 1])
        print(f"\nWrong guesses: {wrong_letters}\n")
        print(result)

        if lives == 0:
            clear_screen()
            text_delay("Sorry out of lives. Better luck next time")
            sys.exit(1)
        elif "_" not in result:
            clear_screen()
            text_delay(f"That's right, the meaning of life is:\n\n{answer}\n\nCongratulations you win!! Bye now")
            sys.exit(1)

        guess = str(input("\nGuess: ")).strip()

        if len(guess) > 1:
            text_delay("One character at a time")
            time.sleep(2)
            clear_screen()
            continue
        elif guess not in LETTERS_ORIGINAL:
            text_delay("That is not a letter")
            time.sleep(2)
            clear_screen()
            continue
        elif guess.lower() in answer.lower():
            letters = letters.replace(guess.lower(), "").replace(guess.upper(), "")
        elif guess.lower() in wrong_letters:
            pass
        else:
            wrong_letters += guess.lower() + " "
            lives -= 1

        clear_screen()

        if lives == 1 and extra_life == 0:
            extra_life += 1
            print(HANGMAN_ASCII[0])
            text_delay("\nOh no you only have 1 life left. I'll give you an extra 2 lives if you answer the following question right but you'll lose the game if you answer incorrectly. Do you accept? ")
            risk = input().lower().strip()

            match extra_life_q(risk):
                case "correct":
                    lives += 2
                case "incorrect":
                    sys.exit(1)

            time.sleep(2)
            clear_screen()


def extra_life_q(risk_it):
    """Offer the player a trivia question to win extra lives."""
    valid_answers = ["a", "b", "c", "d"]

    while True:
        if risk_it == "yes":
            response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple", timeout=10)
            data = response.json()

            question_data = data["results"][0]
            question = html.unescape(question_data["question"])
            correct_answer = html.unescape(question_data["correct_answer"])
            all_answers = [html.unescape(answer) for answer in question_data["incorrect_answers"]]
            all_answers.append(correct_answer)
            random.shuffle(all_answers)

            text_delay(f"\n{question}\n")
            for index, answer in enumerate(all_answers):
                current_letter = chr(index + 97)
                text_delay(f"{current_letter}. {answer}")
            print()

            correct_answer_letter = chr(all_answers.index(correct_answer) + 97)
            user_answer = input("Choose the correct letter: ").strip().lower()

            while user_answer not in valid_answers:
                user_answer = input("Choose the correct letter: ").strip().lower()

            if user_answer == correct_answer_letter:
                text_delay("\nWell look at you smarty pants. Okay you get back two lives")
                return "correct"
            else:
                text_delay("\nYeah that is not the correct answer. Bye bye now")
                return "incorrect"

        elif risk_it == "no":
            return "pass"

        else:
            text_delay("\nIt's a yes or no question dear")
            risk_it = input().lower().strip()


def tea(tea_choice):
    """Validate the tea choice and return the matching innkeeper response."""
    tea_choice = tea_choice.lower().strip()

    if tea_choice.endswith(" tea"):
        tea_choice = tea_choice.replace(" tea", "")

    while tea_choice not in TEA_LIST:
        text_delay("I've never heard of that, try again dear")
        tea_choice = input().lower().strip()

        if tea_choice.endswith(" tea"):
            tea_choice = tea_choice.replace(" tea", "")

    if tea_choice == "english breakfast":
        return TEA_DIALOGUE[1]
    return TEA_DIALOGUE[0]
