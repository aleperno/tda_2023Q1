from aux import prepare_scenarios, measure_time
from functools import reduce
from algorithms import greedy_algorithm, greddy_alternative, dynamic_programming

test_scenarios = prepare_scenarios('test_cases.csv')

for scenario, cases in test_scenarios.items():
    products = cases['packages']
    asked_bribe = cases['bribe']
    
    print(f"----------------------\nSCENARIO: {scenario}")
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
