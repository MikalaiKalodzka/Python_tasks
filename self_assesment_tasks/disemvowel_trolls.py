"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata 'y' isn't considered a vowel.
"""
import re

def remove_vowel(text):
    """
    Takes string text and returns string text without vowels.
    :param text: string
    :return: string
    """

    vowel_list = 'aeiou'
    result = ''
    for symbol in text:
        if symbol not in vowel_list:
            result += symbol
        else:
            continue
    return result


given_text = 'Trolls are attacking your comment section!'
# given_text = ''
print(remove_vowel(given_text))

# REGULAR EXPRESSIONS
result = re.findall(r'[^aeiou]', given_text)
print(''.join(result))
