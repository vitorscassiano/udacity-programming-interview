"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(array, value):
    copy = array
    while len(array) >= 1:
        mid = len(array)//2

        if value == array[mid]:
            return copy.index(array[mid])
        elif value < array[mid]:
            array = array[:mid]
        elif value > array[mid]:
            array = array[mid+1:]
    return -1


test_list = [1,3,9,11,15,19,29,30]
test_val1 = 25
test_val2 = 19

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
