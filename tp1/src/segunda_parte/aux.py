import random
from functools import reduce
from clases import Bribe, Product

MAX_QTY = 10
MAX_PACKAGES = 100
MAX_TYPES = 30

def create_bribes(products):
    bribes = []
    for i in range(0, MAX_TYPES + 1):
        if(random.random() > 0.7):
            continue
        product_types = list(filter(lambda prod: prod.prod_type == i, products))
        if(product_types == []):
            continue
        in_stock = reduce(lambda acum, prod: acum + prod.qty, product_types, 0)
        bribes.append(Bribe(i, random.randint(1, in_stock)))
    return bribes

def create_products():
    return [Product(random.randint(0, MAX_TYPES), random.randint(1, MAX_QTY)) for i in range(MAX_PACKAGES)]


def products_map(products):
    available_products = {}
    for prod in products:
        if(prod.prod_type in available_products):
            available_products[prod.prod_type].append(prod)
        else:
            available_products[prod.prod_type] = [prod]
            
    return available_products