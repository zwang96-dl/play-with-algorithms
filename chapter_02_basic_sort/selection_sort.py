from sort_test_helper.helpers import generate_random_array
from sort_test_helper.helpers import test_sort


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    n = 10000
    arr = generate_random_array(n, 0, n)
    test_sort('selection_sort', selection_sort, arr)