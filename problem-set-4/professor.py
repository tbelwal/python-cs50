# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
import random


def main():
    n = get_level()
    score = 0

    for _ in range(10):
        if ask_questions(n):
            score += 1

    print("Score: ", score)


def ask_questions(n):
    rand_x = generate_integer(n)
    rand_y = generate_integer(n)

    for _ in range(3):
        try:
            answer = int(input(f"{rand_x} + {rand_y} = "))
        except ValueError:
            print("EEE")
            continue

        if answer == (rand_x + rand_y):
            return True
        print("EEE")

    print(f"{rand_x} + {rand_y} = {rand_y + rand_x}")
    return False


def get_level():
    while True:
        try:
            level = int(input(("Level: ")))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(n):
    start = 0 if n == 1 else 10 ** (n - 1)
    stop = 10**n - 1

    return random.randint(start, stop)


if __name__ == "__main__":
    main()
