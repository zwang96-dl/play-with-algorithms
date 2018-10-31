from sort_test_helper.helpers import generate_random_array
from sort_test_helper.helpers import generate_nearly_ordered_random_array
from sort_test_helper.helpers import test_sort
from chapter_02_basic_sort.selection_sort import selection_sort
from chapter_02_basic_sort.insertion_sort import insertion_sort


if __name__ == '__main__':
    n = 10000
    arr1 = generate_random_array(n, 0, n)

    test_sort('selection_sort', selection_sort, arr1[:])
    test_sort('insertion_sort', insertion_sort, arr1[:])

    arr2 = generate_nearly_ordered_random_array(n, 0, n, 1)
    test_sort('selection_sort (nearly sorted array)', selection_sort, arr2[:])
    test_sort('insertion_sort (nearly sorted array)', insertion_sort, arr2[:])