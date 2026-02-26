def is_even(number: int) -> bool:
    """Return True if number is even."""
    return number % 2 == 0


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Even" if is_even(num) else "Odd")