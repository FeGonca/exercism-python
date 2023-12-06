"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
import lasagna

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(layers):
    """Calculate the total preparation time for all layers.

    :param layers: list - number of layers in each recipe.
    :return: int - total preparation time (in minutes).
    
    This function calculates the total preparation time needed by adding up
    the preparation times for each layer. The value returned should be the sum
    of the preparation times multiplied by the number of layers.
    """

    return layers * PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time for all steps involved with making the lasagna.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    This function calculates the total elapsed time by adding up the preparation time
    needed for each layer plus the time spent baking the lasagna so far.
    """

    # Calculate the total preparation time required for all layers
    total_preparation_time = preparation_time_in_minutes(number_of_layers)

    # Add the elapsed bake time to get the total elapsed time
    total_elapsed_time = total_preparation_time + elapsed_bake_time

    return total_elapsed_time


