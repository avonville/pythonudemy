from random import randint


def set_difficulty():
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print(f"Invalid input. Exiting...")
        exit()


def check_answer(guess, answer, attempts):
    if guess > answer:
        print(f"Too high.")
        return attempts - 1
    elif guess < answer:
        print(f"Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        exit()


def play_game():
    print(f"Welcome to the Number Guessing Game!")

    print(f"I'm thinking of a number between 1 and 100.")

    number = randint(1, 100)
    attempts = set_difficulty()
    guess = 0

    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input(f"Make a guess: "))
        attempts = check_answer(guess, number, attempts)
        if attempts == 0:
            print(f"You've run out of guesses, you lose.")
            print(f"The answer was {number}.")
            exit()
        elif guess != number:
            print(f"Guess again.")


play_game()
