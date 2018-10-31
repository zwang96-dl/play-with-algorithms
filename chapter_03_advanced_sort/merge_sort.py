from chapter_02_basic_sort.insertion_sort import insertion_sort_in_range


def merge_sort(arr):
    __merge_sort(arr, 0, len(arr) - 1)

def __merge_sort(arr, l, r):
    """递归使用归并排序，对arr[l...r]的范围进行排序"""
    if r - l <= 15:
        insertion_sort_in_range(arr, l, r)
        return
    mid = l + (r - l) // 2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid + 1, r)
    __merge(arr, l, mid, r)

def __merge(arr, l, mid, r):
    """将arr[l...mid]和arr[mid+1...r]两部分进行归并"""
    aux = [arr[i] for i in range(l, r + 1)]
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if i > mid:
            arr[k] = aux[j - l]
            j += 1
        elif j > r:
            arr[k] = aux[i - l]
            i += 1
        elif aux[i - l] < aux[j - l]:
            arr[k] = aux[i - l]
            i += 1
        else:
            arr[k] = aux[j - l]
            j += 1

def merge_sort_bu(arr):
    """自底向上的归并排序"""
    sz = 1
    while sz <= len(arr):
        i = 0
        while i + sz < len(arr):
            # 对arr[i...i+sz-1]和arr[i+sz...i+2*sz-1]
            __merge(arr, i, i + sz - 1, min(i + 2 * sz - 1, len(arr) - 1))
            i += 2 * sz
        sz += sz
