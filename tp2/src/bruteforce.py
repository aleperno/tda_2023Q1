from itertools import permutations
from collections import deque
from data import generate_random_data
from copy import deepcopy


def smartpack(items):
    """
    Performs a 'smart' packing approximation

     - Sorts the items in descending order
     - Start with a pack, inserting elements from left to right (from 'heavier' to 'lighter')
     - If the current leftmost item doesn't fit the pack, we start inspecting elements from right to left
       (from lighter to heavier).
     - If the rightmost (lightest) item fits the pack, insert it and continue; if not close it and start a new pack
       with the leftmost item.

    Time Complexity Analysis
     - Sorting: O(N * log(N))
     - Packing: O(N)

     Overall: O(N * log(N))
    """

    # Sorting and Setup Stage
    new_items = deque(sorted(items, reverse=True))
    aux = deepcopy(new_items)
    packages = []

    package = []
    package_size = 0

    # Packing Stage
    while new_items:
        l = new_items.popleft()
        if package_size + l <= 1:
            package_size += l
            package.append(l)
            continue
        else:
            # Must check if the rightmost item fits
            while new_items and new_items[-1] + package_size <= 1:
                r = new_items.pop()
                package_size += r
                package.append(r)

            packages.append(package)
            package = [l]
            package_size = l

    packages.append(package)
    return packages


def pack(items):
    """
    Packs a given set of items

    Uses the following logic
        - Open a pack and insert an item
        - While items fix in the pack, insert them
        - If an item doesn't fit, close the pack, open a new one and continue the same operation
          until all items are packed

    Returns the set of packs

    This operation is O(n) where n is the ammout of items.
    """
    packages = []

    package = []
    package_size = 0

    for item in items:  # O(N)
        if package_size + item <= 1:
            # If it fits...I sits.
            package_size += item
            package.append(item)
        else:
            # Need new package
            packages.append(package)
            package = [item]
            package_size = item

    packages.append(package)

    return packages


def bruteforce(items):
    """
    Bruteforces the pack approximation

    The `pack` methods uses an approximation which its solution quality heavily relies
    in the dataset order. We can assert for for any given collection of items, there's a specific
    order of those elements which the `pack` approximation gives the optimal solution.

    Therefore the bruteforce uses ALL possible permutations of a given set to feed the method, and records which
    result is best

    For a set of N elements, there are N! (factorial(n)) permutations, all of size N and no repetitions.
    """
    permutated_items = permutations(items)
    current_solution = None
    current_value = 0

    for item_set in permutated_items:
        #print('foo')
        new_result = pack(item_set)
        new_value = len(new_result)
        if not current_solution or new_value < current_value:
            current_solution = new_result
            current_value = new_value

    return current_solution


def main():
    while True:
        #data = generate_random_data(4)
        data = [0.99, 0.1]
        optimo = bruteforce(data)
        n_optimo = len(optimo)
        aprox = pack(data)
        n_aprox = len(aprox)

        relacion = n_aprox / n_optimo
        print(f"La relacion es {relacion}")
        if relacion > 2:
            print(data)
            break

        break


if __name__ == '__main__':
    main()
