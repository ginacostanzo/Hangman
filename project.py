import sys
import random
from hangman import categories, HANGMANPICS


def main():
    count = 0
    print("Welcome to hangman. You will have 6 chances to guess letters in the word." + "\n" + "If you think you know the word, type it in. If you guess the word and guess wrong, you will automatically lose.")
    category = input("Choose one of the following categories or type 'new' to enter a new list of words." + "\n" + "-fruits" + "\n" + "-states" + "\n" + "-random" + "\n" + "Category: ")
    if category.lower() == "new":
        words = input("Enter the words you wish to play with separated by commas: ")
        words_list = format(words)
    else:
        words_list = categories[category]
    word = random.choice(words_list).strip().lower()
    print(HANGMANPICS[count] + "  " + "_ " * len(word))
    display = ["_"] * len(word)
    guessed = []
    while True:
        guess = input("Guess a letter: ").lower()
        if validate(guess, word):
            if len(guess) == 1:
                if check_letter(guess, word, display, guessed) == "q":
                    break
            if len(guess) == len(word):
                count = len(guessed)
                print(HANGMANPICS[count] + " " + "  " + word)
                print(check_word(guess, word))
                break

def format(words):
    if "," in words:
        new_words = words.split(",")
        return new_words
    else:
        sys.exit("Invalid format. Words must be separated by commas.")

def validate(guess, word):
    if len(guess) == 1 or len(guess) == len(word):
        return True
    else:
        print("Guess must be 1 letter, space, or whole word.")
        return False

def check_letter(guess, word, display, guessed):
    if guess in word:
        index = 0
        count = len(guessed)
        for index in range(len(word)):
            if word[index] == guess:
                display[index] = display[index].replace("_", guess)
                index += 1
        print(HANGMANPICS[count] + " " + "  ".join(display) + "\n" + ", ".join(guessed))
        return "c"
    elif guess not in word:
        if guess not in guessed:
            guessed.append(guess)
        count = len(guessed)
        if count < 6:
            print(HANGMANPICS[count] + " " + "  ".join(display) + "\n" + ", ".join(guessed))
            return "c"
        elif count == 6:
            print(HANGMANPICS[count] + " " + "  " + word + "\n" + "You lose.")
            return "q"

def check_word(guess, word):
    if guess.strip() == word.strip():
        return "You win!"
    else:
        return "You lose."


if __name__ == "__main__":
    main()
