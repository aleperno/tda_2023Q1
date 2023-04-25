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


def main():
    result = merge_sort(LISTAS, k_merge)
    expected = list(sorted(itertools.chain(*LISTAS)))

    assert result == expected

main()
