import random
from argparse import ArgumentParser, ArgumentTypeError


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


def check_pos_int(value):
    try:
        value = int(value)
        if value <= 0:
            raise ArgumentTypeError(f"{value} is not a positive integer")
        else:
            return value
    except ValueError:
        raise Exception(f"{value} not an integer")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-n', '--number', type=check_pos_int, default=5, required=False)
    return parser.parse_args()


def main():
    args = parse_args()
    data = generate_random_data(length=args.number)
    print(f"{len(data)}\n")
    for object in data:
        print(object)


if __name__ == '__main__':
    main()
