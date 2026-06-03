# Answer to Life


def main():
    user_answer = (
        input(
            "What is your answer to the Great Question of Life, the Universe and Everything?"
        )
        .lower()
        .strip()
    )

    print(evaluate_answer(user_answer))


def evaluate_answer(ans):
    match ans:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


main()
