from sort_test_helper.helpers import generate_random_array
from sort_test_helper.helpers import test_sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 寻找元素arr[i]合适的插入位置
        temp = arr[i]
        index = i
        for j in range(i, 0, -1):
            if temp < arr[j - 1]:
                arr[j] = arr[j - 1]
                index = j - 1
            else:
                break
        arr[index] = temp

def insertion_sort_in_range(arr, l, r):
    for i in range(l + 1, r + 1):
        # 寻找元素arr[i]合适的插入位置
        temp = arr[i]
        index = i
        for j in range(i, l, -1):
            if temp < arr[j - 1]:
                arr[j] = arr[j - 1]
                index = j - 1
            else:
                break
        arr[index] = temp
