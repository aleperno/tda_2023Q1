from itertools import permutations
from collections import deque
from copy import deepcopy


def sumfloat(x, y, decimals=4):
    """
    Sums two floats, taking into account a maximum of decimals in order to avoid
    floating point errors
    """
    return round(x + y, decimals)


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

        new_size = sumfloat(package_size, l)
        if new_size <= 1:
            package_size = new_size
            package.append(l)
            continue
        else:
            # Must check if the rightmost item fits
            while new_items and sumfloat(new_items[-1], package_size) <= 1:
                r = new_items.pop()
                package_size = sumfloat(package_size, r)
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
        new_size = sumfloat(package_size, item)
        if new_size <= 1:
            # If it fits...I sits.
            package_size = new_size
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
        new_result = pack(item_set)
        new_value = len(new_result)
        if not current_solution or new_value < current_value:
            current_solution = new_result
            current_value = new_value

    return current_solution


def main():
    pass

if __name__ == '__main__':
    main()
