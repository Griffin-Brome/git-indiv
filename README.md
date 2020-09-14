# COSC 499 Git Assignment

This is a simple implementation of a top-down merge sort as outlined in [this article] (https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation_using_lists). It currently supports integers, which it sorts in _ascending_ order.

## Methods

### merge_sort()

This method is the main caller method in the program. It recursively calls itself on each half of the input array, then uses the `merge()` helper method to join them.

### merge()

This is a helper method that takes two sorted lists and combines them into one sorted list.
