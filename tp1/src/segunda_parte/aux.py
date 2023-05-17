import random
from functools import reduce
from clases import Bribe, Product
import pandas as pd
import time


MAX_QTY = 20
MAX_PACKAGES = 5
MAX_TYPES = 2

def create_bribes(products, max_types = MAX_TYPES):
    bribes = []
    for i in range(1, max_types + 1):
        # if(random.random() > 0.7):
        #     continue
        product_types = list(filter(lambda prod: prod.prod_type == i, products))
        if(product_types == []):
            continue
        in_stock = reduce(lambda acum, prod: acum + prod.qty, product_types, 0)
        bribes.append(Bribe(i, random.randint(1, in_stock)))
    return bribes

def create_products(max_types=MAX_TYPES, max_qty=MAX_QTY, max_packages=MAX_PACKAGES):
    return [Product(random.randint(1, max_types), random.randint(1, max_qty)) for i in range(max_packages)]


def products_map(products):
    available_products = {}
    for prod in products:
        if(prod.prod_type in available_products):
            available_products[prod.prod_type].append(prod)
        else:
            available_products[prod.prod_type] = [prod]
            
    return available_products


def prepare_scenarios(source_file):
    df = pd.read_csv(source_file, sep=',')

    scenarios = {}
    for scenario in df.scenario.unique():
        scenarios[scenario] = {}
        cases = df[df.scenario == scenario]
        scenario_packages = []
        scenario_bribes = []
        for _, test_case in cases.iterrows():
            prod_type = test_case.type
            scenario_packages += [Product(prod_type, int(qty)) for qty in test_case.packages.split(";")]
            scenario_bribes += [Bribe(prod_type, int(test_case.bribe))]
        scenarios[scenario] = {'packages':scenario_packages, 'bribe': scenario_bribes}
    return scenarios

def measure_time(test_func, bribes, products):
    start = time.process_time()
    result = test_func(bribes, products)
    end = time.process_time()
    return result, end-start