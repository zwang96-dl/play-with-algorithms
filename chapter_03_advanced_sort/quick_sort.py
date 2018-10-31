import random
from time import time

from chapter_02_basic_sort.insertion_sort import insertion_sort_in_range


def quick_sort(arr):
    random.seed(time())
    __quick_sort(arr, 0, len(arr) - 1)

def __quick_sort(arr, l, r):
    """对arr[l...r]前闭后闭部分进行快速排序"""
    if l >= r:
        return
    p = __partition(arr, l, r)
    __quick_sort(arr, l, p - 1)
    __quick_sort(arr, p + 1, r)

def __partition(arr, l, r):
    """
    对arr[l...r]前闭后闭部分进行partition操作，
    返回p, 使得arr[l...p-1] < arr[p], 并且arr[p+1...r] > arr[p]
    """
    _random_index = random.randint(l, r)
    arr[l], arr[_random_index] = arr[_random_index], arr[l]
    pivot_value = arr[l]
    # arr[l+1...j] < pivot_value; arr[j+1...i) > pivot_value
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < pivot_value:
            # now the element at j + 1 is definitely <= v!!!
            # so safe to swap
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort2(arr):
    """双路快排 quick sort two ways"""
    random.seed(time())
    __quick_sort2(arr, 0, len(arr) - 1)

def __quick_sort2(arr, l, r):
    """对arr[l...r]前闭后闭部分进行快速排序"""
    if l >= r:
        return
    p = __partition2(arr, l, r)
    __quick_sort2(arr, l, p - 1)
    __quick_sort2(arr, p + 1, r)

def __partition2(arr, l, r):
    """
    对arr[l...r]前闭后闭部分进行partition操作，
    返回p, 使得arr[l...p-1] < arr[p], 并且arr[p+1...r] > arr[p]
    """
    _random_index = random.randint(l, r)
    arr[l], arr[_random_index] = arr[_random_index], arr[l]
    pivot_value = arr[l]
    # arr[l+1...i) <= pivot_value, arr(j...r] >= pivot_value
    i, j = l + 1, r # initial ranges both empty
    while True:
        while i <= r and arr[i] < pivot_value:
            i += 1
        while j >= l + 1 and arr[j] > pivot_value:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort_3_ways(arr):
    """三路快排"""
    random.seed(time())
    __quick_sort_3_ways(arr, 0, len(arr) - 1)

def __quick_sort_3_ways(arr, l, r):
    """
    三路快速排序处理arr[l...r]
    将arr[l...r]分为 (1) 小于pivot_value, (2) 等于pivot_value, (3) 大于pivot_value三部分
    之后递归对小于pivot_value部分和大于pivot_value部分分别继续进行三路快速排序
    """
    if r - l <= 15:
        insertion_sort_in_range(arr, l, r)
        return
    # partition部分
    _random_index = random.randint(l, r)
    arr[l], arr[_random_index] = arr[_random_index], arr[l]
    pivot_value = arr[l]
    lt = l      # arr[l+1...lt] < pivot_value
    gt = r + 1  # arr[gt...r] > pivot_value
    i = l + 1   # arr[lt+1...i) == pivot_value, i is current index
    while i < gt:
        if arr[i] < pivot_value:
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot_value:
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else: # arr[i] == pivot_value
            i += 1
    arr[l], arr[lt] = arr[lt], arr[l]
    __quick_sort_3_ways(arr, l, lt - 1)
    __quick_sort_3_ways(arr, gt, r)
