import time
from functools import reduce
from copy import deepcopy
from aux import create_bribes, create_products, products_map

def greedy_algorithm(products, asked_bribe):
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = sorted(available_products[prod], key=lambda x: x.qty, reverse=False)

    bribes = {}
    for bribe in asked_bribe:
        bribed = 0
        bribes[bribe.prod_type] = []
        for product in available_products[bribe.prod_type]:
            if(bribed <= bribe.qty):
                bribes[bribe.prod_type].append(product)
                bribed += product.qty
            if bribed == bribe.qty:
                break
    return bribes


def greddy_alternative(products, asked_bribe):
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = sorted(available_products[prod], key=lambda x: x.qty, reverse=True)

    bribes = {}
    for bribe in asked_bribe:
        bribed = bribe.qty
        bribes[bribe.prod_type] = []
        total_packages = reduce(lambda acum, prod: acum + prod.qty, available_products[bribe.prod_type], 0)
        for product in available_products[bribe.prod_type]:
            total_packages = total_packages - product.qty

            if(total_packages == 0):
                if(bribed <= 0):
                    continue
                else:
                    bribes[bribe.prod_type].append(product)
                    bribed -= product.qty
            else:
                relation_w_remain = bribed/total_packages   
                if(relation_w_remain > 1):
                    bribes[bribe.prod_type].append(product)
                    bribed -= product.qty
                else:
                    continue

    return bribes


def payments_grid(products, bribe):
    max_prod = reduce(lambda acum, prod: acum + prod.qty, products, 0)
    table = [[bribe.qty for x in range(max_prod + 1)] for x in range(len(products) + 1)] 
    for row in range(len(products)+1):
        for column in range(max_prod + 1):
            if(row == 0 or column == 0):
                continue
            elif(column >= products[row-1].qty):
                table[row][column] = min(table[row-1][column-products[row-1].qty] - products[row-1].qty, table[row-1][column])
            else:
                table[row][column] = table[row-1][column]
    return table


def recurr_pay_bribe(table, product_idx, bribe_idx, products):
    if(product_idx == 0):
        return []
    "No se uso el producto"
    if(table[product_idx-1][bribe_idx] == table[product_idx][bribe_idx]):
        return recurr_pay_bribe(table, product_idx -1, bribe_idx, products)
    else:
        "Uso el producto para pagar el soborno"
        product = products[product_idx-1]
        return [product] + recurr_pay_bribe(table, product_idx -1, bribe_idx - products[product_idx-1].qty, products)


def dynamic_programming(products, bribes):
    """
    Ecuación de Recurrencia:
        OPT(n, bribe.qty) = MIN
            - No usar el producto: OPT(n-1, bribe.qty)
            - Usar el producto: OPT(n-1, bribe.qty - pj.qty) + pj.qty
    """
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = list(sorted(available_products[prod], key=lambda x: x.qty, reverse=True))
    
    all_bribes = {}
    for bribe in bribes:
        type_products = available_products[bribe.prod_type]
        table = payments_grid(type_products, bribe)
        
        best_match = -1
        for idx,diff in enumerate(table[len(type_products)]):
            if(diff <= 0):
                best_match = idx
                break
        product_bribes = recurr_pay_bribe(table, len(type_products), best_match, type_products)
        all_bribes[bribe.prod_type] = product_bribes
    return all_bribes
        

def measure_time(test_func, bribes, products):
    start = time.process_time()
    result = test_func(bribes, products)
    end = time.process_time()
    return result, end-start


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
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units")


    print("\nGREEDY ALT")
    bribes, res_time = measure_time(greddy_alternative, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units")

    print("\nDYNAMIC")
    bribes, res_time = measure_time(dynamic_programming, products, asked_bribe)
    print(f"\nDelerivered as bribe, in {res_time}")
    for prod_type,bribes in bribes.items():
        total = reduce(lambda acum, prod: acum + prod.qty, bribes, 0)
        print(f"product type: {prod_type} delivered: {total} packages in {len(bribes)} units")

