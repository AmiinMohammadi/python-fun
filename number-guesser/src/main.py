import random


def check_guess(guess, min_range, max_range):

    try:
        num = int(guess)
        if min_range <= num <= max_range:
            return num, ""
        return -1, "Guess must be between 0 to 100\nTry Again"

    except ValueError:
        return -1, "Guess must be number\nTry Again"


def show_score(text, score):
    print("—————————————————————")
    print(f"{text}: {score}")
    print("—————————————————————")


def main():

    START_RANGE = 0
    END_RANGE = 100
    user_score = 10

    rnd_num = random.randint(START_RANGE, END_RANGE)

    while True:

        user_guess, error_text = check_guess(
            input("\nenter your new guess: "), START_RANGE, END_RANGE
        )

        if error_text:
            print(error_text)
            continue

        if user_guess == rnd_num:
            print("Correct Answer!\nYou won")
            show_score("Your score: ", user_score)
            break

        if (user_score := user_score - 1) == 0:
            print("You don't have a chance.\nGame Over!")
            show_score("Your score: ", user_score)
            break

        print("Oh Missing answer...\nYou lost one point")

        if user_guess < rnd_num:
            print("Hint: it's larger")

        else:
            print("Hint: it's less than")

        show_score("Your chances: ", user_score)


if __name__ == "__main__":
    main()
