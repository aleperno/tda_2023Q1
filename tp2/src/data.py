import random


def random_item(decimals=2):
    """
    Returns Random float value between (0, 1]

    `random.random` returns a value between [0, 1) therefore we use the substraction to 1 to do the inverse.
    Then we multiply by 100, convert to int and divide by 100 to truncate the float to two decimal places.

    """
    rounding_factor = 10**decimals

    return int((1-random.random()) * rounding_factor) / rounding_factor


def generate_random_data(length=10, decimals=2):
    return [random_item(decimals) for i in range(length)]


class LengthMismatch(Exception):
    pass


def read_data_file(path):
    total_elements = 0
    data = []

    with open(path, 'r') as f:
        # Number of elements
        total_elements = int(f.readline().splitlines()[0])

        # Blank line
        f.readline()

        # Read remaining elements

        for line in f:
            data.append(float(line))

    if total_elements != len(data):
        raise LengthMismatch()

    return data
