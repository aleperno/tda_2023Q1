from functools import reduce
from aux import create_bribes, create_products, measure_time
from algorithms import greedy_algorithm, greddy_alternative, dynamic_programming, dynamic_programming_iterative


if __name__ == '__main__':

    products = create_products()
    asked_bribe = create_bribes(products)

    print("Available Products:\n")
    [print(prod) for prod in sorted(products, key=lambda x: x.prod_type)]
    print("\nBribes:\n")
    [print(bribe) for bribe in asked_bribe]

    print("\nGREEDY")
    bribes, res_time = measure_time(greedy_algorithm, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        a = ",".join(list(map(lambda x: str(x.qty), bribes)))
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units {a}")


    print("\nGREEDY ALT")
    bribes, res_time = measure_time(greddy_alternative, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        a = ",".join(list(map(lambda x: str(x.qty), bribes)))
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units {a}")
        

    print("\nDYNAMIC")
    bribes, res_time = measure_time(dynamic_programming, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        a = ",".join(list(map(lambda x: str(x.qty), bribes)))
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units {a}")


    print("\nDYNAMIC ITERATIVE")
    bribes, res_time = measure_time(dynamic_programming_iterative, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        a = ",".join(list(map(lambda x: str(x.qty), bribes)))
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units {a}")


