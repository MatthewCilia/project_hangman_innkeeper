# 🕹️ Meaning of Life Hangman Adventure
#### Video Demo: https://youtu.be/fRiV4N2YSOI
#### Description:

## 💡 The Idea

I decided I want to do a simple game of hangman as it seemed like a good project to do. However I did have a concern that it is not complex enough compared to how other alumni of the course reinterpreted the game of hangman, I looked into how to make a unique version of hangman.

## 🔧 The Design

After checking out other projects I finally decided that I would do an interactive story version of hangman where the player has travelled far and wide to discover the meaning of life. The game starts off at the innkeeper’s inn where the player knocks and is met with the innkeeper. This gave the game more charm than just a simple hangman game and allowed me to include storytelling which is a hobby of mine. I also gave the text a delay effect as you see in other games so the text doesn’t feel so abrupt when presented.

### 🧙‍♂️ The Innkeeper

The innkeeper asks players yes or no questions and if the player responds with anything else they are re-prompted until they enter yes or no. Depending on the answer the user chooses the game will either progress or end. I had the idea to make it so the user can write anything and as long as there is yes or no in the answer it counts. But I went against this as if the user says “Yes I would not like to do that” the program will take that as a yes, even though it's a no, so I kept it more simple, even if it is more rigid.

### ☕️ The Tea

At some point the player is asked what tea they would like and after picking a tea they are told that only English Breakfast is available. Eventually the innkeeper loads the hangman game so that the player can discover the meaning of life. ASCII art of the hangman is displayed and each time there is a wrong guess it changes to the next ASCII art. The wrong guesses are displayed so that the user can keep track. Each time a correct guess is given the phrase starts to reveal itself. When anything else aside from a single letter is inputted by the user, the game informs the user to only put one letter at a time.

### 💖 The Extra Lives

If the user only has one life left (Player has 7 lives in total which are represented by the ASCII art) the user is prompted warning them and offering them to answer a random multiple choice question to get 2 lives back. This is only available once per run through. If answered incorrectly the player loses the game. Initially I had one set question but decided to use an API to get random questions each playthrough to keep the game more interesting.

## 📜 The Conclusion

I had some other ideas like giving the user the chance to guess the phrase immediately and if guessed correctly they are given a fun fact but didn’t want to overcomplicate the game too much so kept it a bit more simple.

## 📁 The Files

 The drumroll.mp3 and the partyblower.mp3 are sound effects that play when introducing the game. “project.py“ runs the meaning of life hangman game and “test_project.py” tests it.

