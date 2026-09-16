import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "internet"]

# Select a random word
secret_word = random.choice(words)

# Display underscores for each letter
display_word = ["_"] * len(secret_word)

# Track guessed letters
guessed_letters = set()

# Maximum incorrect guesses
incorrect_guesses = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < 6 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Check whether the letter is in the word
    if guess in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\n🎉 You won!")
    print("The word was:", secret_word)
else:
    print("\n😢 You lost!")
    print("The word was:", secret_word)