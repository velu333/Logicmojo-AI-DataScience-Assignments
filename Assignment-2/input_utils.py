def get_positive_integer(prompt: str) -> int:
    """
    Prompt the user until a valid positive integer is entered.

    Parameters
    ----------
    prompt : str
        The message displayed to the user.

    Returns
    -------
    int
        A positive integer entered by the user.
    """

    # Get user input for n
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                print(f"Invalid input. Please enter a positive integer greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
