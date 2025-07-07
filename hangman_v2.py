import random
import string
from time import sleep
from os import system 
from wordfreq import top_n_list

# Function to clear the console
def clear():
    system('cls')

# Clear the console at the start
clear()

def hangman():
    # Get the top 5000 common English words
    word_list = top_n_list('en', 5000)

    # Filter words with length greater than 5 and less than 10
    words = [word for word in word_list if 5 < len(word) < 10]

    # Shuffle the filtered word list
    random.shuffle(words)

    # Removes "illegal" words (x-ray, etc.)
    for i in words:
        for letter in i:
            if letter not in string.ascii_lowercase:
                words.remove(i)
                break

    # Select a random word from the filtered word list
    word = random.choice(words)

    # Create a list of underscores with the same length as the selected word
    blanks = ['_' for _ in word]

    # Initialize the number of attempts
    attempts = 6

    # Initialize the guessed letters list
    guessed_letters = []

    # Function to print the current state of blanks
    def print_blanks():
        print("\n\n")
        for blank in blanks:
            print(blank, end=' ')
        print("\n")
        print("Guessed letters: ", end='')
        print(', '.join(guessed_letters))
        print()

    # Print the initial state of blanks
    print_blanks()

    # Print a newline
    print()

    # List of lowercase alphabets
    alphabets = list(string.ascii_lowercase)

    # Function to wait, clear the console, and print the current state of blanks
    def do_():
        sleep(1.3)
        clear()
        print_blanks()
        print()

    # Loop until the number of attempts is greater than 0 and there are blanks
    while ('_' in blanks):
        letter = input("Enter a letter: ").lower()
        print()

        # Check if the input is a valid alphabet letter
        if letter not in alphabets:
            print("Please enter a valid alphabet letter.")
            print()
            do_()
            continue

        # Check if the letter has already been guessed
        elif letter in guessed_letters:
            print("You have already guessed this letter.")
            do_()
            continue

        # Check if the letter is in the word
        elif letter in word:
            print(f"Nice Guess! {letter} is in the word.")
            print()
            guessed_letters.append(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    blanks[i] = letter

        # Check if the input is more than one letter
        elif len(letter) > 1:
            print("Please enter only one letter.")
            print()
            do_()
            continue

        # Check if the letter is not in the word
        elif letter not in word:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
            print()
            guessed_letters.append(letter)

        # Break the loop if attempts run out
        if attempts == 0:
            break

        # Wait, clear the console, and print the current state of blanks
        do_()

    # Check if the player has won or lost
    if attempts != 0:
        print("Congratulations! You have guessed the word.")
        print()
    else:
        print("You have run out of attempts.")
        print()
        print(f"The word was {word}.")
        print("Better luck next time!\n")

# Main loop to play the game repeatedly
while True:
    hangman()
    print("Thank you for playing Hangman.")
    option = input("Do you want to play again? (y/n): ").lower()
    if option != 'y':
        break
    clear()

# Print goodbye message at the end
print("\n\nGoodbye!")  

# # End of the program