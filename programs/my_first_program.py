from nada_dsl import *


def nada_main():
    """
    Defines the main computation logic for the program.

    This function takes two secret integers my_int1 and my_int2 as inputs
    and performs their multiplication, storing the result in a secret output
    variable my_output.

    Raises:
        ValueError: If the multiplication operation overflows the supported
                    integer range.
    """

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))


    # Perform multiplication with error handling for overflow
    try:
        my_output = my_int1 * my_int2
    except OverflowError:
        raise ValueError("Multiplication result overflows supported integer range.")

    return [Output(my_output, "my_output", party1)]