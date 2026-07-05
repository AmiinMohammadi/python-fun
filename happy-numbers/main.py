"""Author: https://github.com/Taha-26"""


def is_happy(number: int) -> bool:
    """Determine if a positive integer is a happy number.

    A happy number is defined by the following process:
    Starting with any positive integer, replace the number by the sum of
    the squares of its digits, and repeat the process until the number
    equals 1 (where it will stay), or it loops endlessly in a cycle
    which does not include 1.

    :param number: The positive integer to check.
    :return: True if the number is happy, False otherwise.
    """

    # Track already visited numbers to detect infinite loops.
    seen_numbers = set()

    # Continue until number reaches 1 or a cycle is detected.
    while (number != 1) and (number not in seen_numbers):
        seen_numbers.add(number)

        # Calculate the sum of the squares of each digit
        number = sum(int(i) ** 2 for i in str(number))

    return number == 1


def main():
    # 7 is a happy, will return True
    print(is_happy(7))

    # 44 is a happy, will return True
    print(is_happy(44))

    # 4 is not a happy number (enters a cycle), will return False
    print(is_happy(4))


if __name__ == "__main__":
    main()
