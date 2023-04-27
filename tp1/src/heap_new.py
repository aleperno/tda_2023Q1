import heapq


def heap_sort(arrays):
    """
     - Arrays: List of K ordered lists of H elements.
    """
    non_empty_list_count = len(arrays)  # O(1)
    aux = len(arrays)
    result = []

    heap = [(n, arrays[i]) for i, n in enumerate(next(zip(*arrays)))]  # O(K)
    heapq.heapify(heap)  # O(K)

    while non_empty_list_count:  # O(K*H)
        smallest, lst = heapq.heappop(heap)  # O(log(K))
        result.append(smallest)  # O(1)
        lst.popleft()  # O(1)

        if lst:
            # Sigue habiendo elementos
            heapq.heappush(heap, (lst[0], lst))  # O(log(K))
        else:
            non_empty_list_count -= 1

    while heap:  # O(K)
        # assert len(heap) == aux
        smallest, lst = heapq.heappop(heap)  # O(log(K))
        result.append(smallest)

    return result
