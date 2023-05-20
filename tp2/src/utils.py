import time
from copy import deepcopy


def perform_time_test(test_func, dataset, pre=None, post=None):
    dataset_copy = deepcopy(dataset)
    start = time.process_time()
    result = test_func(dataset_copy)
    end = time.process_time()

    return result, end-start
