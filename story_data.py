"""Text, constants, and ASCII art used by the game."""

RULES = [
    "Rule 1: Guess one letter at a time until you solve the hidden phrase.",
    "Rule 2: Every time you make an incorrect guess, I'll add more to the hangman and if I can't add any more, you lose.",
]

MEANINGS_OF_LIFE = [
    "Fried chicken",
    "You will always have stress so stop stressing",
    "Do not open the box",
    "Legends are not born, they are made",
    "Your side hustle will succeed so yes quit your job",
]

HANGMAN_ASCII = [r"""
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

INNKEEPER_DIALOGUE_YES = [
    "Ahh, hello traveller. I see you have travelled far and wide to come here. I presume you are here to learn about the meaning of life?",
    "Wonderful! Well, why don’t you come in and I’ll make you some tea to warm you back up. What tea do you prefer?",
    "*The innkeeper leaves*\n*Do you open the box?*",
    "*Innkeeper returns*\nHere's your tea, and that's the meaning of life! Oh look at that face! Don't worry, I'm only joking. But I can't just give you the meaning of life—you'll have to play a game of hangman to uncover it. So, what do you say? Are you up for it?",
    "Excellent! Let's go for",
]

INNKEEPER_DIALOGUE_NO = [
    "Oh, okay. Well then, on your way you go. Safe travels.\n",
    "",
    "Inside the black box, you find a black hole which sucks you in. You are lost in a dark space for eternity. Don’t touch other people’s stuff.\nGAME OVER\n",
    "Well, in that case, we will just enjoy this tea. *Sips tea* Delicious!\n",
]

TEA_LIST = [
    "english breakfast", "earl grey", "green", "oolong", "white", "chamomile",
    "peppermint", "jasmine", "chai", "darjeeling", "assam", "sencha",
    "matcha", "genmaicha", "pu-erh", "lemongrass", "rooibos", "hibiscus",
    "yerba mate", "ginger",
]

TEA_DIALOGUE = [
    "Oh, that sounds delicious! But I only have English Breakfast. Stay right there and I'll get it for you. Oh, and don't open the black box.",
    "Oh good, that's all I have! Stay right there and I'll get it for you. Oh, and don't open the black box.",
]

LETTERS_ORIGINAL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
