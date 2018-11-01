import random

from chapter_04_heap_sort.heap_sort import MaxHeap
from chapter_04_heap_sort.heap_sort import heap_sort1
from chapter_04_heap_sort.heap_sort import heap_sort2
from sort_test_helper.helpers import generate_random_array
from sort_test_helper.helpers import generate_nearly_ordered_random_array
from sort_test_helper.helpers import test_sort
from chapter_03_advanced_sort.merge_sort import merge_sort
from chapter_03_advanced_sort.quick_sort import quick_sort
from chapter_03_advanced_sort.quick_sort import quick_sort_3_ways


if __name__ == '__main__':
    n = 10000

    # test 1
    arr1 = generate_random_array(n, 0, n)
    test_sort('merge_sort', merge_sort, arr1[:])
    test_sort('quick_sort', quick_sort, arr1[:])
    test_sort('quick_sort_3_ways', quick_sort_3_ways, arr1[:])
    test_sort('heap_sort1', heap_sort1, arr1[:])
    test_sort('heap_sort2', heap_sort2, arr1[:])
    print('*' * 20)

    # test 2
    arr2 = generate_nearly_ordered_random_array(n, 0, n, 0)
    test_sort('merge_sort', merge_sort, arr2[:])
    test_sort('quick_sort', quick_sort, arr2[:])
    test_sort('quick_sort_3_ways', quick_sort_3_ways, arr2[:])
    test_sort('heap_sort1', heap_sort1, arr2[:])
    test_sort('heap_sort2', heap_sort2, arr2[:])
    print('*' * 20)

    # test 3
    arr3 = generate_nearly_ordered_random_array(n, 0, n, 500)
    test_sort('merge_sort', merge_sort, arr3[:])
    test_sort('quick_sort', quick_sort, arr3[:])
    test_sort('quick_sort_3_ways', quick_sort_3_ways, arr3[:])
    test_sort('heap_sort1', heap_sort1, arr3[:])
    test_sort('heap_sort2', heap_sort2, arr3[:])
    print('*' * 20)






