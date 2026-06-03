# 1. Prompt user for game level n - range for guessing
# 2. If the user does not input a positive integer, the program should prompt again.
# 3. Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
# 4. Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#         If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#         If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#         If the guess is the same as that integer, the program should output Just right! and exit.
import random


def main():
    n = get_level()
    get_guesses(n)


def get_level():
    while True:
        try:
            game_level = int(input(("Level: ")))
            if game_level >= 1:
                return game_level
        except ValueError:
            continue


def get_guesses(n):
    random_number = random.randrange(1, n + 1)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess == random_number:
                    print("Just right!")
                    return
                elif guess > random_number:
                    print("Too large!")
                else:
                    print("Too small!")
        except ValueError:
            continue


if __name__ == "__main__":
    main()
