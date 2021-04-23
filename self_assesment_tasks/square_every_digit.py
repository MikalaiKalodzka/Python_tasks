"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_every_digit():
    non_digit = True
    digit_number = ''
    while non_digit:
        digit_number = input("Input your number: ")
        if digit_number.isdigit():
            non_digit = False
            break
        else:
            print("Input correct number, please: ")
            continue
    print(f'Your input number is {digit_number}')

    digit_str = ''
    for digit in digit_number:
        digit_str += str((int(digit))**2)

    return f'Result number is {int(digit_str)}'


print(square_every_digit())