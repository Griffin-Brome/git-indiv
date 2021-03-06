"""
COSC 499 Individual Git Assignment
Author: Griffin Brome | 63057285

This is a simple python program that can take a list of integers, and either
sort them ascendingly or descendingly. Both of these are done using merge sort
"""

def merge_sort(input_list):
    """
    Takes a list of length 'n' of integers as list and sorts them

    This is done using Merge Sort, more information on the algorithm can be 
    found here: https://en.wikipedia.org/wiki/Merge_sort
    """ 

    if len(input_list) <= 1:
        return input_list
    else:
        left = input_list[0:int(len(input_list)/2)]
        right = input_list[int(len(input_list)/2):len(input_list)]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


def merge(left, right):
    """
    Helper method that merges two sorted lists into one list
    """
    
    merged_list = []
    
    while len(left) > 0  and len(right) > 0:
        if left[0] <= right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))

    if len(left) != 0:
        merged_list.extend(left)
    elif len(right) !=0:
        merged_list.extend(right)

    return merged_list


def reverse_merge_sort(input_list):
    """ Does the same as merge_sort() except (you guessed it) in reverse """
    
    if len(input_list) <= 1:
        return input_list
    else:
        left = input_list[0:int(len(input_list)/2)]
        right = input_list[int(len(input_list)/2):len(input_list)]

        left = reverse_merge_sort(left)
        right = reverse_merge_sort(right)

        return reverse_merge(left, right)
    pass


def reverse_merge(left, right):
    """ Helper for reverse_merge_sort() """
    
    merged_list = []
    
    while len(left) > 0  and len(right) > 0:
        if left[0] >= right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))

    if len(left) != 0:
        merged_list.extend(left)
    elif len(right) !=0:
        merged_list.extend(right)

    return merged_list
    pass
