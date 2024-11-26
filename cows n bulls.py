import random

def get_feedback(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(c), guess.count(c)) for c in set(guess)) - bulls
    return bulls, cows

def cows_and_bulls():
    words = ['apple', 'grape', 'peach', 'berry', 'melon']
    score = 0
    
    print("Welcome to Cows and Bulls!")
    
    while True:
        secret_word = random.choice(words)
        attempts = 0
        
        print("\nTry to guess the secret word (5 letters).")
        print("For each guess, you will receive feedback in the form of:")
        print("Bulls: Correct letters in the correct position")
        print("Cows: Correct letters in the wrong position")
        
        while True:
            guess = input("Enter your guess (5 letters): ").lower()
            
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid input. Please enter a 5-letter word.")
                continue
            
            attempts += 1
            bulls, cows = get_feedback(secret_word, guess)
            
            print(f"{bulls} Bulls, {cows} Cows")
            
            if bulls == 5:
                print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
                score += 1
                break
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break
    
    print(f"Your final score: {score} {'round' if score == 1 else 'rounds'} played.")
    print("Thank you for playing!")

if __name__ == "__main__":
    cows_and_bulls()