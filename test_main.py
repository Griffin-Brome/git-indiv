"""
Pytest tests for main.py
"""

from main import *

# this is a change

def test_merge():
    left = [1,7,9,20]
    right = [3,5,15]

    assert merge(left, right) == [1,3,5,7,9,15,20]


def test_merge_sort():
    unsorted_list = [2,3,8,15,1,3]
    assert merge_sort(unsorted_list) == [1,2,3,3,8,15]


def test_reverse_merge():
    left = [9,7,3,2]
    right = [32,15,4]
    assert reverse_merge(left, right) == [32,15,9,7,4,3,2]


def test_reverse_merge_sort():
    unsorted_list = [1,8,2,18,94,32,2,3]
    assert reverse_merge_sort(unsorted_list) == [94,32,18,8,3,2,2,1]
