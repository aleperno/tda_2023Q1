"""
Merge Sorting K-Sorted Arrays

Time Complexity Considerations:

  We've taken into account Python Official docs https://wiki.python.org/moin/TimeComplexity for builtin classes like
  list and deque; and heapq code https://github.com/python/cpython/blob/3.10/Lib/heapq.py for the heapq module.

  - list:
    - append: O(1)
    - length: O(1)
  - deque:
    - popleft: O(1)
    - length: O(1)


Here we use list and dequeue almost interchangeable when performing the merge, however there is one big difference
between them that must be noted. Index access to an element of the list l[k] is O(1); whereas access to a deque element
deque[k] is O(n) where n is the size of the array (https://docs.python.org/3/library/collections.html#collections.deque)
depending on the index we're trying to access.

Therefore instead of the more common approach for the merge using index accesses, we use iterators that have a far
better performance, both for lists and deques. A test for this can be found in the notebooks folder.
"""
from typing import List, Deque, Tuple


def k_merge(left: List[int] | Deque[int], right: List[int] | Deque[int]) -> Tuple[List[int], int]:
    """
    Merges two sorted arrays of int

    This implementation uses iterators and may be confusing if used to the implementation using indexes.
     - We have the 'current values' for both `left` and `right` arrays, we compare them and add the lowest one to the
       results list.
     - We update the current value for the set we inserted into the results, with the next value in the original set.
       E.G: current_left resulted lower than current_right, therefore we insert current_left into the results list,
       and then set `current_left = next(iter_left)` both updating the value and advancing in the iteration
     - We perform these steps until one of the iterators raises an StopIteration. Since the 'current values' were gotten
       by the `next` function which advances the iterator, before consuming the remaining iterator we mast add one of
       the `current_values`.
       E.G: `next(iter_left)` raises StopIteration, therefore before adding all the remaining elements in `iter_right`
            to the results_list, we must add the `current_right` value to the list.
    """
    ops = 0
    result = []
    iter_left = iter(left)
    iter_right = iter(right)
    current_left = next(iter_left)
    current_right = next(iter_right)

    while True:
        ops += 1
        if current_left < current_right:
            try:
                result.append(current_left)
                current_left = next(iter_left)
            except StopIteration:
                result.append(current_right)
                ops += 1
                break
        else:
            try:
                result.append(current_right)
                current_right = next(iter_right)
            except StopIteration:
                result.append(current_left)
                ops += 1
                break

    for l in iter_left:
        ops += 1
        result.append(l)

    for r in iter_right:
        ops += 1
        result.append(r)

    assert ops == len(left) + len(right)
    return result, ops


def merge_sort(arrays, merge_func=k_merge):
    """
    Performs the Merge-Sort of a given set of arrays
    """
    ops = 0
    length = len(arrays)

    if length == 1:
        return arrays[0], 1

    half = length // 2
    left = arrays[:half]
    right = arrays[half:]

    ops += length

    sorted_left, l_ops = merge_sort(left, merge_func)
    sorted_right, r_ops = merge_sort(right, merge_func)

    ops += l_ops
    ops += r_ops

    result, merge_ops = merge_func(sorted_left, sorted_right)
    ops += merge_ops

    return result, ops
