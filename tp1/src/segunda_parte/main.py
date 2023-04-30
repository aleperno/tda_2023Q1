import random
from aux import create_bribes, create_products

def greedy_algorithm(products, asked_bribe):
    available_products = {}
    for prod in products:
        if(prod.prod_type in available_products):
            available_products[prod.prod_type].append(prod)
        else:
            available_products[prod.prod_type] = [prod]
            
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


if __name__ == '__main__':

    products = create_products()
    asked_bribe = create_bribes(products)

    print("Available Products:\n")
    [print(prod) for prod in sorted(products, key=lambda x: x.prod_type)]
    print("\nBribes:\n")
    [print(bribe) for bribe in asked_bribe]

    bribes, remaining = greedy_algorithm(products, asked_bribe)
    print("\nDelerivered as bribe")
    [print(bribe) for bribe in bribes]
    print("\nTo be Kept:\n")
    [print(remain) for remain in remaining]
