"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

"""


def snail_sort(num_list, snail_list):

    if not num_list:
        return snail_list
    for num in range(len(num_list[0])):
        snail_list.append(num_list[0][num])
        num_list[0][num] = 'x'
    if len(num_list) > 2:
        for num in range(1, len(num_list) - 1):
            snail_list.append(num_list[num][-1])
            num_list[num][-1] = 'x'

    for num in range(len(num_list[-1]) - 1, -1, -1):
        snail_list.append(num_list[-1][num])
        num_list[-1][num] = 'x'
    for num in range(len(num_list) - 2, 0, -1):
        if num_list[num][0] != 'x':
            snail_list.append(num_list[num][0])
            num_list[num][0] = 'x'
        else:
            break
    # delete all used numbers that now are useless
    for i in num_list:
        while 'x' in i:
            i.remove('x')

    while 'x' in snail_list:f
        snail_list.remove('x')

    # delete all empty elements in the list
    while [] in num_list:
        num_list.remove([])

    return snail_sort(num_list, snail_list)


# test_list = []
# test_list = [[]]
# test_list = [[1, 2]]
test_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in test_list:
    print(i)
print()
print(snail_sort(test_list, []))
print(test_list)