"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often
 referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def camel_case(text):
    """
    Takes string text and returns it camel case string version
    :param text: string
    :return: string
    """
    if '-' in text:
        text_list = text.split('-')
    elif '_' in text:
        text_list = text.split('_')

    for i in range(len(text_list)):
        if i == 0:
            if text_list[i].lower():
                text_list[i] = text_list[i]
            else:
                text_list[i] = text_list[i].capitalize()
        else:
            text_list[i] = text_list[i].capitalize()
    result = ''.join(text_list)
    return result


# example = "the-stealth-warrior"
example = "The_Stealth_Warrior"
print(camel_case(example))
