from sort_test_helper.helpers import generate_random_array
from sort_test_helper.helpers import generate_nearly_ordered_random_array
from sort_test_helper.helpers import test_sort
from chapter_02_basic_sort.insertion_sort import insertion_sort
from chapter_03_advanced_sort.merge_sort import merge_sort
from chapter_03_advanced_sort.merge_sort import merge_sort_bu
from chapter_03_advanced_sort.quick_sort import quick_sort
from chapter_03_advanced_sort.quick_sort import quick_sort2
from chapter_03_advanced_sort.quick_sort import quick_sort_3_ways


if __name__ == '__main__':
    n = 10000
    arr1 = generate_random_array(n, 0, n)

    test_sort('merge_sort', merge_sort, arr1[:])
    test_sort('merge_sort_bu', merge_sort_bu, arr1[:])
    # test_sort('insertion_sort', insertion_sort, arr1[:])
    test_sort('quick_sort', quick_sort, arr1[:])

    arr2 = generate_nearly_ordered_random_array(n, 0, n, 10)
    test_sort('merge_sort', merge_sort, arr2[:])
    test_sort('merge_sort_bu', merge_sort_bu, arr2[:])
    # 退化到O(n^2)的概率非常非常小
    test_sort('quick_sort', quick_sort, arr2[:])

    arr2 = generate_random_array(n, 0, 10)
    test_sort('merge_sort', merge_sort, arr2[:])
    test_sort('merge_sort_bu', merge_sort_bu, arr2[:])
    # 退化到O(n^2)的概率非常非常小
    test_sort('quick_sort', quick_sort, arr2[:])
    test_sort('quick_sort2', quick_sort2, arr2[:])
    test_sort('quick_sort_3_ways', quick_sort_3_ways, arr2[:])