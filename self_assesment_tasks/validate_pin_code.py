"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
import re


def validate_pin_code(pin_string):
    """
    Takes string as a pin code and returns boolean value whether it is valid or not.
    :param pin_string: string
    :return: boolean
    """
    valid = True
    length = len(pin_string)
    if not pin_string.isdigit():
        valid = False
        print("Incorrect PIN. Should be only digits.")
        return valid
    elif length not in [4, 6]:
        valid = False
        print("Incorrect PIN. Should be 4 or 6 digits.")
        return valid
    else:
        print("Your PIN is valid.")
        return valid


def user_input():
    """
    Takes none and returns string user input.
    :return: string
    """
    user_pin = input("Input your PIN code: ")
    return user_pin


value = False
while not value:
    pin = user_input()
    value = validate_pin_code(pin)

    print('\n')

    # REGULAR EXPRESSION

    if re.match(r'[\d]{4}$', pin) or re.match(r'[\d]{6}$', pin):
        print('Valid')
    else:
        print('Not Valid')
