
():
    # 1. Use a small list of 5 predefined words
    words = ["cherry", "kavya", "hasini", "mango"]
    target_word = random.choice(words)
    guessed_letters = []
    # 2. Limit incorrect guesses to 6
    attempts_remaining = 6

    print("--- Welcome to Hangman! ---")

    # 3. Basic console input/output loop
    while attempts_remaining > 0:
        # Display current progress
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check if the player won
        if "_" not in display_word:
            print("Congratulations! You won!")
            return

        # Handle user input
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        # Logic for correct/incorrect guesses
        if guess in target_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not there.")

    print(f"\nGame Over! The word was: {target_word}")

if __name__ == "__main__":
    play_hangman()
    
