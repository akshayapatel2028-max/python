import random

# List of words
words = ["apple", "mango", "banana", "orange", "grapes"]

# Select a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:
    display = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is completely guessed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts Left:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)