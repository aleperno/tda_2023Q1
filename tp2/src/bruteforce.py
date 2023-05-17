from itertools import permutations
from collections import deque
from data import generate_random_data
from copy import deepcopy


def smartpack(items):
    new_items = deque(sorted(items, reverse=True))
    aux = deepcopy(new_items)
    packages = []

    package = []
    package_size = 0

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
    packages = []

    package = []
    package_size = 0

    for item in items:
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



#print(bruteforce([0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]))
#data = [0.11, 0.9, 0.11, 0.9, 0.11, 0.9]
#data = generate_random_data(10)
data = [0.8, 0.59, 0.98, 0.8, 0.0, 0.89, 0.63, 0.87, 0.31, 0.92]

#print(pack(data))
#print(bruteforce(data))
#print(smartpack(data))


while True:
    #data = generate_random_data(4)
    data = [0.99, 0.1, 0.99, 0.1, 0.99, 0.1, 0.99, 0.1, 0.99, 0.1, 0.99, 0.1]
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

