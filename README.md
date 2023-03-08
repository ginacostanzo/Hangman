# Hangman

#### Video Demo: https://youtu.be/okdtd5jLeWE

#### Description:
This is the game hangman. This program comes with a few built in lists of words with the option to add your own word list.
## project.py
This file contains 5 functions.
### main
The main function prompts the user for a word category from the existing lists or a new word list. If the user enters a new word list, the format function will be called. Then random will choose a random word from the word list and that will be the word for the game. It initializes a guessed variable to be an empty list that will later contain the user's incorrect guesses and initializes a display variable that starts out as "_" to represent each letter in the word. Then it begins a while loop to continue prompting the user for a guess until they either guess the word or run out of guesses.
### format
This will use the split method to separate the user's list of words at the commas. If the user did not enter their words separated by commas, they will receive an error message and the program will exit.
### validate
This will validate a user's guess. The guess must be either 1 single character or match the exact length of the word. If it does not, they will receive an error message and be prompted to guess again.
### check_letter
This will check the user's guess if their guess is 1 single character in length. If their guess is in the word, it will find the position of the guessed character in the word and replace the display at that location with the guess. It will continue this until it checks every letter in the word to make sure that duplicates of the same letter are counted. If the user's guess is not in the word, the count will increase by 1. If the count is less than 6, they will be prompted to guess again and the previous display will be shown to them again with a new hangman part added. If the count is equal to 6, they have run out of guesses and will be shown the word and the message "You lose."
### check_word
This will check the user's guess if it is the length of the whole word. If their guess matches the word, they will be shown the message "You win!". If it doesn't, they will automatically lose. They will be shown the word and the message "You lose."

## test_project.py
This file contains all of the tests for the custom functions in project.py

## hangman.py
This file contains a list of the hangman ASCII art for each body part and a dictionary of lists for each built in category for the game.