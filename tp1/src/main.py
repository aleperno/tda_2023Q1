"""
Complexity Analysis

1) Pseudo Merge-Sort
 - N: Problem Size
 - a: Subproblems per recursion
 - b: How much the problem is being reduced by each recursion. n/b is the size of the subproblems
 - f(n): Work done outside the recursion stages

 a=2, b=2; f(n)=N

 T(N) = 2 * T(N/2) + N

 Comparing n ^(log_b (a)) con f(n)

 N^(log_2(2)) = N; entonces T(n) = O(n * log(n))


2) Heaps Algorithm

 T(n) = O(n * log(k))

"""
import random
import itertools
import time
from copy import deepcopy
from collections import deque
from heap import heap_sort
from merge_sorts import merge_sort


K = 4
H = 10


def create_test_dataset(k=K, h=H):
    return [deque(sorted(random.randint(0, 100) for _ in range(h))) for _ in range(k)]


def perform_time_test(test_func, dataset, pre=None, post=None):
    dataset_copy = deepcopy(dataset)
    start = time.process_time()
    result, ops = test_func(dataset_copy)
    end = time.process_time()

    return result, end-start, ops


def main():
    dataset = create_test_dataset()
    print("Testing Merge Sort")
    result, res_time, ops = perform_time_test(merge_sort, dataset)
    print(f"Merge Sort lasted {res_time} and did {ops} ops")

    print("Testing Heap Sort")
    result_heaps, res_time, ops = perform_time_test(heap_sort, dataset)
    print(f"Heap Sort lasted {res_time} and did {ops} ops")

    expected = list(sorted(itertools.chain(*dataset)))

    assert result == expected
    assert result_heaps == expected


if __name__ == '__main__':
    main()
