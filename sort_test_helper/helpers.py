import random
from time import time
from random import randint


def generate_random_array(n, range_l, range_r):
    random.seed(time())
    return [randint(range_l, range_r) for _ in range(n)]

def test_sort(sort_name, sort_func, arr):
    start_time = time()
    sort_func(arr)
    print('<{}> function costs {:.5f} seconds to sort a length of {} array.'.format(
        sort_name,
        time() - start_time,
        len(arr),
    ))
    assert is_sorted(arr), '<{}> is wrong!'.format(sort_name)
    
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True