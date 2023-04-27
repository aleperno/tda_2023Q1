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
import time
from copy import deepcopy
from collections import deque
from heap_new import heap_sort as new_heap_sort
from merge_sorts import merge_sort


K = 12800
H = 100


def create_test_dataset(k=K, h=H):
    return [deque(sorted(random.randint(0, 100) for _ in range(h))) for _ in range(k)]


def perform_time_test(test_func, dataset):
    dataset_copy = deepcopy(dataset)
    start = time.process_time()
    result = test_func(dataset_copy)
    end = time.process_time()

    return result, end-start


def main():
    dataset = create_test_dataset()
    print("Probando Merge Sort")
    result, res_time = perform_time_test(merge_sort, dataset)
    print(f"Merge Sort tardó {res_time}")

    #result_heap = heap_sort(LISTAS)
    print("Probando el Heap Sort")
    result_new_heap, res_time = perform_time_test(new_heap_sort, dataset)
    print(f"Heap Sort tardó {res_time}")

    expected = list(sorted(itertools.chain(*dataset)))

    assert result == expected
    #assert result_heap == expected
    assert result_new_heap == expected


if __name__ == '__main__':
    main()
