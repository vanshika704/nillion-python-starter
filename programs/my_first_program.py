from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform addition, subtraction, multiplication, and division
    addition_result = my_int1 + my_int2
    subtraction_result = my_int1 - my_int2
    multiplication_result = my_int1 * my_int2
    division_result = my_int1 / my_int2  # Note: Division assumes my_int2 is non-zero

    # Define outputs
    outputs = [
        Output(addition_result, "addition_output", party1),
        Output(subtraction_result, "subtraction_output", party1),
        Output(multiplication_result, "multiplication_output", party1),
        Output(division_result, "division_output", party1)
    ]

    return outputs

