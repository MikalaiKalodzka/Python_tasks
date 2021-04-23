"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which
is the number of times you must multiply the digits in num until you reach a single digit.
"""
from main import integer_input_in_string_format


def persistence_bugger():
    input_number = integer_input_in_string_format()
    mult_count = 0
    if int(input_number) % 10 == int(input_number):
        return mult_count
    not_single_digit = True

    while not_single_digit:
        input_number = str(input_number)
        multiplication = 1
        for item in input_number:
            multiplication *= int(item)

        if multiplication % 10 == multiplication:
            mult_count += 1
            return mult_count
        else:
            mult_count += 1
            input_number = multiplication


print(persistence_bugger())