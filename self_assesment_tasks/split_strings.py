"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') // should return ['ab', 'c_']
solution('abcdef') // should return ['ab', 'cd', 'ef']
"""
import re


def split_strings(text):
    """
    Takes string text and returns a list of its paired characters. If there is no pair to the last character, function
    adds '_' to it.
    :param text: string
    :return: list of strings
    """
    length = len(text)
    if length % 2 != 0:
        text += '_'

    text_list = []
    for i in range(0, length, 2):
        text_list.append(text[i:i+2])
    return text_list


example = 'abc'
# example = 'abcdefgh'
print(split_strings(example))

print('\n')
# REGULAR EXPRESSION
result = re.findall(r'\w\w', example)
if len(result) % 2 == 0:
    print(result)
else:
    result[-1] += '_'
