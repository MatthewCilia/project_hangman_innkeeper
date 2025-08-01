import sys
import re
import os
import time
import pyfiglet
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from random import choice

# Rules of the game
rules = [
    "Rule 1: Guess one letter at a time until you solve the hidden phrase",
    "Rule 2: Everytime you make an incorrect guess, I'll add more to the hangman and if I can't add any more, you lose"
]
MoL = [
    "Fried chicken",
    "You will always have stress so stop stressing",
    "Do not open the box",
    "Legends are not born, they are made",
    "Your side hustle will succeed so yes quit your job"
]
hangman_ascii = [r"""
  +---+
  |   |
  |   O
  |  /|\
  |  / \
  |
=========""", r"""
  +---+
  |   |
  |   O
  |  /|\
  |  /
  |
=========""", r"""
  +---+
  |   |
  |   O
  |  /|\
  |
  |
=========""", r"""
  +---+
  |   |
  |   O
  |  /|
  |
  |
=========""", """
  +---+
  |   |
  |   O
  |   |
  |
  |
=========""", """
  +---+
  |   |
  |   O
  |   
  |
  |
=========""", """
  +---+
  |   |
  |
  |
  |
  |
========="""
]
innkeeper_dial_yes = [
    "Ahh, hello traveller. I see you have travelled far and wide to come here. I presume you are here to learn about the meaning of life?",
    "Wonderful! Well, why don’t you come in and I’ll make you some tea to warm you back up. What tea do you prefer?",
    "*The innkeeper leaves*\n*Do you open the box?*",
    "*Innkeeper returns*\nHere's your tea, and that's the meaning of life! Oh look at that face! Don't worry, I'm only joking. But I can't just give you the meaning of life—you'll have to play a game of hangman to uncover it. So, what do you say? Are you up for it?",
    "Excellent! Let's go for"
]
innkeeper_dial_no = [
    "Oh, okay. Well then, on your way you go. Safe travels.\n",
    "",
    "Inside the black box, you find a black hole which sucks you in. You are lost in a dark space for eternity. Don’t touch other people’s stuff.\nGAME OVER\n",
    "Well, in that case, we will just enjoy this tea. *Sips tea* Delicious!\n"
]
tea_list = [
    "english breakfast",
    "earl grey",
    "green tea",
    "oolong tea",
    "white tea",
    "chamomile",
    "peppermint",
    "jasmine tea",
    "chai tea",
    "darjeeling",
    "assam",
    "sencha",
    "matcha",
    "genmaicha",
    "pu-erh",
    "lemongrass tea",
    "rooibos",
    "hibiscus tea",
    "yerba mate",
    "ginger tea"
]
tea_dial = [
    "Oh, that sounds delicious! But I only have English Breakfast. Stay right there and I'll get it for you. Oh, and don't open the black box.",
    "Oh good, that's all I have! Stay right there and I'll get it for you. Oh, and don't open the black box."
]
letters_original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = choice(MoL)

def main():
    clear_screen()
    innkeeper_dialogue()
    game_start()
    hangman()
    
# This runs the hangman game
def hangman():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lives = 7
    extra_life= 0
    wrong_letters = ""
    
    # Generates the visuals
    while True:
        result = re.sub("[" + letters + "]", "_", ans)
        print(hangman_ascii[lives-1])
        print(f"\nWrong guesses: {wrong_letters}\n")
        print(result)
        
        # Checks if you win or lose
        if lives == 0:
            clear_screen()
            text_delay("Sorry out of lives. Better luck next time")
            sys.exit(1)
        elif "_" not in result:
            clear_screen()
            text_delay(f"That's right, the meaning of life is:\n\n{ans}\n\nCongratulations you win!! Bye now")
            sys.exit(1)
        
        guess = str(input("\nGuess: ")).strip()
        
        # Checks the guess
        if len(guess) > 1:
            text_delay("One character at a time")
            time.sleep(2)            
            pass
        elif guess not in letters_original:
            text_delay("That is not a letter")
            time.sleep(2)            
            pass
        elif guess.lower() in ans.lower():
            letters = letters.replace(guess, "").replace(guess.upper(), "")
        elif guess.lower() in wrong_letters:
            pass
        else:
            wrong_letters += guess.lower() + " "
            lives -= 1
        
        clear_screen()

        # Gain some extra lives
        if lives == 1 and extra_life == 0:
            extra_life += 1
            match extra_life_q():
                case "correct": lives += 2
                case "incorrect": sys.exit(1)
            time.sleep(2)
            clear_screen()

# Clears the screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# The question that could gain you extra lives
def extra_life_q():
    print(hangman_ascii[0])
    text_delay("Oh no you only have 1 life left. I'll give you an extra 2 lives if you answer the following question right but you'll lose the game if you answer incorrectly. Do you accept? ")
    risk_it = (input()).lower().strip()
    if  risk_it == "yes":
        text_delay("What is the capital city of Canada? ")
        answer = (input()).lower().strip()
        if answer == "ottawa":
            text_delay("Well look at you smarty pants. Okay you get back two lives")
            return "correct"
        else:
            text_delay("Yeah that is not the correct answer. Bye bye now")
            return "incorrect"
    elif risk_it == "no":
        return "pass"
    
# This is to pick a tea
def tea(tea):

    while tea not in tea_list:
        text_delay("I've never heard of that, try again dear")
        tea = input().lower().strip()
    if tea == "english breakfast":
        return tea_dial[1]
    else:
        return tea_dial[0]

# This is the innkeeper dialogue
def innkeeper_dialogue():
    for i, d in enumerate(innkeeper_dial_yes):
        text_delay(d)
        
        # Breaks the loop at the end to skip the input
        if i == len(innkeeper_dial_yes) - 1:
            break

        answer = input().lower().strip()

        # Makes the user input 
        if i != 1:
            while answer not in ("yes", "no"):
                text_delay("It's a yes or no question dear")
                answer = input().lower().strip()
        
        # This runs the tea scenario
        if i == 1:
            text_delay(tea(answer))

        # This runs the black box scenario
        if i == 2:
            answer = "no" if answer == "yes" else "yes"

        # Exits the program when the input is no, with the exception of the black box scenario
        if answer == "no":
            text_delay(innkeeper_dial_no[i])
            sys.exit(1)

# This introduces the hangman game
def game_start():
    # Drumroll
    mixer.init()
    mixer.music.load("drumroll.mp3")
    mixer.music.play()

    #  This is the ...
    for dot in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)
    mixer.music.stop()
    
    clear_screen()

    mixer.music.load("partyblower.mp3")
    mixer.music.play()

    #  Print out the rules of the game
    print("\n", pyfiglet.figlet_format("Hangman", font="banner3-D"))
    time.sleep(1)
    text_delay("Rules are pretty simple. Take a second to read them\n")
    for rule in rules:
        time.sleep(1)
        text_delay(rule)

    time.sleep(3)
    text_delay("Okay lets begin")
    time.sleep(2)
    clear_screen()

# Delays text to give it some character
def text_delay(anim_text):
    for c in anim_text:
        print(c, end="", flush=True)
        time.sleep(0.05)
    print()

if __name__ == "__main__":
    main()
    

