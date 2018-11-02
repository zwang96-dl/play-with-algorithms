import random
from time import time
from random import randint


def generate_random_array(n, range_l, range_r):
    random.seed(time())
    return [randint(range_l, range_r) for _ in range(n)]


def generate_nearly_ordered_random_array(n, range_l, range_r, swap_times):
    random.seed(time())
    ret = [i for i in range(n)]
    for _ in range(swap_times):
        pos_x, pos_y = randint(0, n - 1), randint(0, n - 1)
        ret[pos_x], ret[pos_y] = ret[pos_y], ret[pos_x]
    return ret


def test_sort(sort_name, sort_func, arr):
    start_time = time()
    sort_func(arr)
    print('<{}> costs {:.5f} seconds to sort a length of {} array.'.format(
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


def union_find_test_helper(uf, n, uf_name):
    start_time = time()
    for _ in range(n):
        uf.union(randint(0, n - 1), randint(0, n - 1))
    for _ in range(n):
        uf.is_connected(randint(0, n - 1), randint(0, n - 1))
    print('{} time costs: {:.5f}'.format(uf_name, time() - start_time))