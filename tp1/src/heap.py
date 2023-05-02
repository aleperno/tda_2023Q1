"""
Heap Sorting K-Sorted Arrays

Time Complexity Considerations:

  We've taken into account Python Official docs https://wiki.python.org/moin/TimeComplexity for builtin classes like
  list and deque; and heapq code https://github.com/python/cpython/blob/3.10/Lib/heapq.py for the heapq module.

  - list:
    - append: O(1)
    - length: O(1)
  - deque:
    - popleft: O(1)
    - length: O(1)
  - heapq:
    - heapify: O(log(N))
    - heappop: O(log(N))
    - heappush: O(log(N))
"""
import heapq
from math import log2
from typing import List, Deque, Tuple


def heap_sort(arrays: List[Deque[int]]) -> Tuple[List[int], int]:
    """
     - Arrays: List of K ordered dequeues of H elements.
    """
    non_empty_list_count = len(arrays)  # O(1)

    K = len(arrays)
    result = []

    """
    Heap operations are log_2(n) and since we use a fixed size heap, all operations for heap
    will be of cost log_2(K)
    """
    LOG_K = log2(K)

    """
    Construct the initial heap by removing the first element of each deque: O(K*1)
    """
    heap = [(n, arrays[i]) for i, n in enumerate(l.popleft() for l in arrays)]
    heapq.heapify(heap)  # O(K)

    ops = 0

    while non_empty_list_count:  # O(K*H)
        smallest, lst = heapq.heappop(heap)  # O(log(K))
        result.append(smallest)  # O(1)

        if lst:
            # There are still elements in the original deque
            heapq.heappush(heap, (lst.popleft(), lst))  # O(log(K))
        else:
            # The deque is empty
            non_empty_list_count -= 1

        """
        In each loop at most we perform two O(log(K)) operations,
        one heappop and one heappush
        """
        ops += LOG_K

    return result, ops
