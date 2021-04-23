"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.

Input: 567321
Output: 765321

"""

def rearrange_digits():

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
    digit_list = []
    for digit in digit_number:
        digit_list.append(int(digit))

    digit_list.sort(reverse=True)

    result_number = ''

    for digit in digit_list:
        result_number += str(digit)

    return int(result_number)


print(rearrange_digits())