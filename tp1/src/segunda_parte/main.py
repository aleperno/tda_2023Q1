import random
from functools import reduce
from aux import create_bribes, create_products, products_map

def greedy_algorithm(products, asked_bribe):
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = sorted(available_products[prod], key=lambda x: x.qty, reverse=False)

    bribes = []
    to_keep = []
    for bribe in asked_bribe:
        bribed = 0
        for product in available_products[bribe.prod_type]:
            if(bribed < bribe.qty):
                bribes.append(product)
                bribed += product.qty
            else:
                to_keep.append(product)
    return [bribes, to_keep]


def greddy_alternative(products, asked_bribe):
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = sorted(available_products[prod], key=lambda x: x.qty, reverse=True)

    bribes = []
    to_keep = []
    for bribe in asked_bribe:
        bribed = bribe.qty
        total_packages = reduce(lambda acum, prod: acum + prod.qty, available_products[bribe.prod_type], 0)
        for product in available_products[bribe.prod_type]:
            remain_qty = total_packages - product.qty

            if(remain_qty == 0):
                if(bribed <= 0):
                    to_keep.append(product)
                else:
                    bribes.append(product)
                    bribed -= product.qty
            else:
                relation_w_remain = bribed/remain_qty
                if(relation_w_remain > 1):
                    bribes.append(product)
                    bribed -= product.qty
                else:
                    to_keep.append(product)
            total_packages -= product.qty

    return [bribes, to_keep]


def payments_grid(products, bribe):
    max_qty = max(list(map(lambda x: x.qty, products)) + [bribe.qty])
    table = [[bribe.qty for x in range(max_qty + 1)] for x in range(len(products) + 1)] 
    for row in range(len(products)+1):
        for column in range(max_qty + 1):
            if(row == 0 or column == 0):
                continue
            elif(column >= products[row-1].qty):
                table[row][column] = min(table[row-1][column-products[row-1].qty] - products[row-1].qty, table[row-1][column])
            else:
                table[row][column] = table[row-1][column]
    return table

def dynamic_programming(products, bribes):
    """
    Ecuación de Recurrencia:
        OPT(n, bribe.qty) = MIN
            - No usar el producto: OPT(n-1, bribe.qty)
            - Usar el producto: OPT(n-1, bribe.qty - pj.qty) + pj.qty
    """
    available_products = products_map(products)
    for prod in available_products:
        available_products[prod] = sorted(available_products[prod], key=lambda x: x.qty, reverse=True)
    
    all_bribes = {}
    for bribe in bribes:
        type_products = available_products[bribe.prod_type]
        table = payments_grid(type_products, bribe)
        all_bribes[bribe.prod_type] = recurr_pay_bribe(table, len(type_products), bribe.qty, type_products)
    return all_bribes
        
def recurr_pay_bribe(table, product_idx, bribe_idx, products):
    if(product_idx == 0):
        return []
    "No se uso el producto"    
    if(table[product_idx-1][bribe_idx] == table[product_idx][bribe_idx]):
        return recurr_pay_bribe(table, product_idx -1, bribe_idx, products)
    else:
        "Uso el producto para pagar el soborno"
        product = products[product_idx-1]
        return [product] + recurr_pay_bribe(table, product_idx -1, products[product_idx-1].qty, products)

if __name__ == '__main__':

    products = create_products()
    asked_bribe = create_bribes(products)

    print("Available Products:\n")
    [print(prod) for prod in sorted(products, key=lambda x: x.prod_type)]
    print("\nBribes:\n")
    [print(bribe) for bribe in asked_bribe]

    print("\nGREEDY")
    bribes, remaining = greedy_algorithm(products, asked_bribe)
    print("\nDelerivered as bribe")
    [print(bribe) for bribe in bribes]
    print("\nTo be Kept:\n")
    [print(remain) for remain in remaining]

    print("\nDYNAMIC")
    bribes, remaining = greddy_alternative(products, asked_bribe)
    print("\nDelerivered as bribe")
    [print(bribe) for bribe in bribes]
    print("\nTo be Kept:\n")
    [print(remain) for remain in remaining]
