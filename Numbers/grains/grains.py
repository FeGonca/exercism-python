"""Functions used in preparing Grains.

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

def square(number):
    """
    Calculate the number of grains on a given square of the chessboard.

    :param number: int - the square number (1 to 64).
    :return: int - the number of grains on the given square.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    
    # Calculate the number of grains on the square using the power of 2
    return 2 ** (number - 1)

def total():
    """
    Calculate the total number of grains on the entire chessboard.

    :return: int - the total number of grains on the chessboard.
    """
    # Calculate the total grains by summing up the grains on each square
    return sum(square(number) for number in range(1, 65))
