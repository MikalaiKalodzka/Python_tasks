"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who l
ike an item. It must return the display text as shown in the examples:

likes [] -- must be "no one likes this"
likes ["Peter"] -- must be "Peter likes this"
likes ["Jacob", "Alex"] -- must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] -- must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] -- must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
"""


def like_function(like_list):
    output_string = ''
    if len(like_list) == 0:
        return 'must be no one likes this'
    elif len(like_list) < 4:
        return f'must be "{like_list[0]}, {like_list[1]} and {like_list[2]} like this"'
    else:
        return f'must be "{like_list[0]}, {like_list[1]} and {len(like_list) - 2} others like this"'


like_list = ["Alex", "Jacob", "Mark", "Max", "Steven"]
print(like_function(like_list))