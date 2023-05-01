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


def dynamic_algorithm(products, asked_bribe):
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
    bribes, remaining = dynamic_algorithm(products, asked_bribe)
    print("\nDelerivered as bribe")
    [print(bribe) for bribe in bribes]
    print("\nTo be Kept:\n")
    [print(remain) for remain in remaining]
