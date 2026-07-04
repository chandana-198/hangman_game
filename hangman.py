import random

# List of predefined words
words = ["apple", "python", "computer", "flower", "school"]

# Randomly choose a word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Number of wrong guesses allowed
lives = 6

# Store guessed letters
guessed_letters = []

print("================================")
print("      WELCOME TO HANGMAN")
print("================================")

while lives > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", lives)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong!")
        lives -= 1

    # Check if player won
    if "_" not in guessed_word:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

# If lives become zero
if lives == 0:
    print("\nGame Over!")
    print("The correct word was:", word)