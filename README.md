# COSC 499 Git Assignment

This is a simple implementation of a top-down merge sort as outlined in [this article](https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation_using_lists). It currently supports integers, which it can sort in either _ascending_ or _descending_ order.

## Methods

### `merge_sort(list)`

This method is the main caller method in the program. It recursively calls itself on each half of the input array, then uses the `merge()` helper method to join them.

### `merge(left, right)`

This is a helper method that takes two sorted lists and combines them into one sorted list.

### `reverse_merge_sort(list)`

This method is the same as `merge_sort()`, except it sorts the input list in descending order.

### `reverse_merge(left, right)`

Helper method for `reverse_merge_sort()`. Merges two lists in descending order.

## Files

All code lives inside `main.py`, unit tests are located in `test_main.py`

## Installation

`git clone https://github.com/Griffin-Brome/git-indiv`

`pip3 install -r requirements.txt`
