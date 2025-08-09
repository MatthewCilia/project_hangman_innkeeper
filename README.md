# 🕹️ Meaning of Life Hangman Adventure

The player has travelled to an innkeeper that holds the **Meaning of Life**… but he will only reveal it if you can win a game of Hangman.

## 🎮 Features

* **Interactive Storyline** – Player chats with the innkeeper where their response effects gameplay.
* **Classic Hangman** – Guess the hidden phrase one letter at a time.
* **Extra Life Challenge** – On your last life you can answer a trivia question that gives you 2 extra lives.
* **ASCII Art & Animated Text** – Retro-style presentation.
* **Sound effects** - A few sound effects for more interactive game play.

## 📜 Rules

1. Guess **one letter at a time** to solve the hidden phrase.
2. Each wrong guess brings the hangman closer to completion. Once completed the game ends.

## 🖥 Requirements

* Python **3.12.11+**
* [pygame](https://www.pygame.org/) for sound effects
* [pyfiglet](https://pypi.org/project/pyfiglet/) for ASCII text banners

## ▶️ How to Play

1. Clone or download the repository.
2. Place the required sound files (`drumroll.mp3` and `partyblower.mp3`) in the same folder as the script.
3. Run the game:

```bash
python project.py
```

4. Respond to the innkeeper appropriately. Game will prompt you on how to respond if you are having trouble.

## 📂 File Structure

```
project.py              # Main game script
drumroll.mp3            # Sound effect for suspense
partyblower.mp3         # Sound effect for winning start
README.md               # This file
```

## 🛠 Developer Notes

* The **innkeeper_dialogue()** function runs the interactive story.
* The **hangman()** function controls the hangman game logic.
* The **extra_life_q()** function gives the player the option to recover 2 lives when they only have one life.
* The **tea()** function handles tea selection and validation.
* The **game_start()** function does the sound effects, title and rules for the hangman game.
* The **clear_screen()** function clears the terminal screen when called on.
* The **text_delay()** function prints out text letter by letter, animating it.

## 📜 License

This game is free for personal and educational use.
