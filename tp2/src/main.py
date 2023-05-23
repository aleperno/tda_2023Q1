from algorithms import bruteforce, smartpack, pack
from data import read_data_file
from time import time
from argparse import ArgumentParser


SOLVER_MAPPING = {
    'E': bruteforce,
    'A': pack,
    'A2': smartpack,
}

SOLVER_NAME_MAPPING = {
    'E': 'Solución Exacta',
    'A': 'Solución Aproximada',
    'A2': 'Solución Aproximada Alumnos',
}


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('algorithm', choices=('E', 'A', 'A2'),
                        help='Algorithm to run. E: Exact Algorithm. A: Approximate Algorithm (Next Fit). A2: Custom Approximate Result')
    parser.add_argument('file_path', help='File path for the data file')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Show the actual solution arrengement')
    return parser.parse_args()


def main():
    args = parse_args()
    data = read_data_file(args.file_path)
    start = time()
    solution = SOLVER_MAPPING[args.algorithm](data)
    end = time()
    elapsed_miliseconds = (end - start) * 1000
    n_solution = len(solution)

    print(f"{SOLVER_NAME_MAPPING[args.algorithm]}: {n_solution}")
    if args.verbose:
        for i, package in enumerate(solution, start=1):
            print(f"E{i}: {{{'; '.join((map(str, package)))}}}")
    print(f"{elapsed_miliseconds:0.2f}")


if __name__ == '__main__':
    main()
