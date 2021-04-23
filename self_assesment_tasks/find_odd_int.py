"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_odd_int(number_list):

    for number in number_list:
        count_int = -1
        for item in number_list:
            if number == item:
                count_int += 1
        if count_int % 2 == 0 and count_int != 0:
            return f'First integer that appears an odd number of times is {number}.'

    return 'There is none integer that appears odd number of times.'


number_list = [1, 4, 3, 3, 5, 2, 6, 1, 7, 8, 32, 2, 3, 4]
print(find_odd_int(number_list))