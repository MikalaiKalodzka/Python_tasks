"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.


For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
import re

def extract_domain(url_text):
    """
    Takes URL string and returns string of domain from it.
    :param url_text: string
    :return: string
    """
    domain = ''
    if url_text.startswith('https://www.'):
        for i in range(12, len(url_text)):
            if url_text[i] == '.':
                break
            else:
                domain += url_text[i]
    elif url_text.startswith('http://www.'):
        for i in range(11, len(url_text)):
            if url_text[i] == '.':
                break
            else:
                domain += url_text[i]
    else:
        for i in range(7, len(url_text)):
            if url_text[i] == '.':
                break
            else:
                domain += url_text[i]
    return domain


# text = "http://github.com/carbonfive/raygun"
text = "http://www.zombie-bites.com"
# text = "https://www.cnet.com"
print(extract_domain(text))

print('\n')
# REGULAR EXPRESSION
# result = re.findall(r'\w+://(\w+)\.\w+', text)
result = re.findall(r'(https?:\/\/)?[w]{3}\.([\w+\-]{2,256})\.\w{2,6}', text)
print(result[0][1])
