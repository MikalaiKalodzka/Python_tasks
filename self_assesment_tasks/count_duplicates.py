"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and
lowercase) and numeric digits.

"""


# should be a dictionary with keys as characters and digits, and values as number of times it appears in string.

input_string = "Indivisibilities"


def count_duplicates(user_input, character):
    result_dict = {}
    for item in user_input:
        if item.lower() in result_dict:
            result_dict[item.lower()] += 1
        else:
            result_dict[item.lower()] = 1
    try:
        return result_dict[character.lower()]
    except KeyError:
        print(f"There is no {character.lower()} in '{user_input}'")


print(count_duplicates(input_string, 'b'))