"""
Pytest tests for main.py
"""

from main import *

def test_merge():
    left = [1,7,9,20]
    right = [3,5,15]

    assert merge(left, right) == [1,3,5,7,9,15,20]


def test_merge_sort():
    unsorted_list = [2,3,8,15,1,3]
    assert merge_sort(unsorted_list) == [1,2,3,3,8,15]
