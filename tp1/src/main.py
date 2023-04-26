"""
Analisis de Complejidad

1) Caso base Merge-Sort
 - N: Tamaño del problema
 - a: Subproblemas por recursion
 - b: Cuanto estamos dividiendo el problema en cada recursion. n/b es el tamaño de cada subproblema
 - f(n): Trabajo por fuera de la recursion

 a=2, b=2; f(n)=N

 T(N) = 2 * T(N/2) + N

 Comparo n ^(log_b (a)) con f(n)

 N^(log_2(2)) = N; entonces T(n) = O(n * log(n))


2) K-merge

 - Cantidad de arrays: K
 - Cantidad de elementos por array: H
 - Cantidad total de elementos: K * H

#TODO Terminar

"""
import random
import itertools
from heap import Heap


K = 4
H = 4

LISTAS = [
    sorted(random.randint(0, 100) for _ in range(H)) for _ in range(K)
]


def k_merge(left, right):
    """
    Each of left and right are array of sorted arrays
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort(arrays, merge_func):
    if len(arrays) == 1:
        return arrays[0]

    half = len(arrays) // 2
    left = arrays[:half]
    right = arrays[half:]

    sorted_left = merge_sort(left, merge_func)
    sorted_right = merge_sort(right, merge_func)

    return merge_func(sorted_left, sorted_right)


def k_merge_heap(arrays, heap, result):
    if(len(arrays) == 0):
        for i in range(len(heap.heap)):
            result.append(heap.remove_element(0))
        return
    smallest = heap.remove_element(0)
    for i in arrays:
        if(i[0] == smallest):
            i.pop(0)
            if(len(i) > 0):
                heap.insert_element(i[0])
            break
    arrays = [element for element in arrays if element != []]
    result.append(smallest)
    return k_merge_heap(arrays, heap, result)


def heap_sort(listas):
    arrays = [list(sublist) for sublist in listas]
    result = []
    if(len(arrays) == 1):
        return arrays
    heap = Heap()
    for i in arrays:
        heap.insert_element(i[0])
        continue
    k_merge_heap(arrays, heap, result)
    return result


def main():
    result = merge_sort(LISTAS, k_merge)
    result_heap = heap_sort(LISTAS)
    expected = list(sorted(itertools.chain(*LISTAS)))

    assert result == expected
    assert result_heap == expected

main()
