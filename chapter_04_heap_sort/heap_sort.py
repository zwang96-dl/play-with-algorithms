class MaxHeap:
    def __init__(self, arr=None, capacity=10):
        if not arr:
            # for the convenience of indexing
            self._data = [None] * (capacity + 1)
            self._count = 0
            self._capacity = capacity
        else:
            n = len(arr)
            self._data = [None] * (n + 1)
            for i in range(n):
                self._data[i + 1] = arr[i]
            self._count = n
            self._capacity = n
            for i in range(self._count // 2, 0, -1):
                self._shift_down(i)

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def insert(self, item):
        assert (self._count + 1) <= self._capacity, 'heap is full'
        self._data[self._count + 1] = item
        self._count += 1
        self._shift_up(self._count)

    def extract_max(self):
        assert self._count > 0, 'can not extract_max from empty heap'
        ret = self._data[1]
        self._data[1], self._data[self._count] = self._data[self._count], self._data[1]
        self._count -= 1
        self._shift_down(1)
        return ret

    def _shift_up(self, index):
        # 因为是最大堆，所以父亲节点的值应该要比孩子节点的值要大的
        while index > 1 and self._data[index // 2] < self._data[index]:
            self._data[index // 2], self._data[index] = self._data[index], self._data[index // 2]
            index //= 2

    def _shift_down(self, index):
        while 2 * index <= self._count:
            j = 2 * index # 在此轮循环中，self._data[index]和self._data[j]交换位置
            if j + 1 <= self._count and self._data[j + 1] > self._data[j]:
                j += 1
            if self._data[index] >= self._data[j]:
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j


class IndexMaxHeap:
    def __init__(self, arr=None, capacity=10):
        if not arr:
            # for the convenience of indexing
            self._data = [None] * (capacity + 1)
            self._indexes = [0] * (capacity + 1)
            self._reverse = [0] * (capacity + 1)
            self._count = 0
            self._capacity = capacity
        else:
            n = len(arr)
            self._data = [None] * (n + 1)
            self._indexes = [0] * (capacity + 1)
            for i in range(n):
                self._data[i + 1] = arr[i]
            self._count = n
            self._capacity = n
            for i in range(self._count // 2, 0, -1):
                self._shift_down(i)

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    # 传入的i对用户而言，是从0索引的
    def insert(self, i, item):
        assert self._count + 1 <= self._capacity, 'heap is full'
        assert i + 1 >= 1 and i + 1 <= self._capacity, 'invalid index'
        i += 1
        self._data[i] = item
        self._indexes[self._count + 1] = i
        self._reverse[i] = self._count + 1
        self._count += 1
        self._shift_up(self._count)

    def extract_max(self):
        assert self._count > 0, 'can not extract_max from empty heap'
        ret = self._data[self._indexes[1]]
        self._data[self._indexes[1]], self._data[self._indexes[self._count]] = self._data[self._indexes[self._count]], self._data[self._indexes[1]]
        self._reverse[self._indexes[1]] = 1
        self._reverse[self._indexes[self._count]] = 0
        self._count -= 1
        self._shift_down(1)
        return ret

    def extract_max_index(self):
        assert self._count > 0, 'can not extract_max from empty heap'
        ret_index = self._indexes[1] - 1
        self._data[self._indexes[1]], self._data[self._indexes[self._count]] = self._data[self._indexes[self._count]], self._data[self._indexes[1]]
        self._reverse[self._indexes[1]] = 1
        self._reverse[self._indexes[self._count]] = 0
        self._count -= 1
        self._shift_down(1)
        return ret_index

    def _contains(self, i):
        assert i + 1 >= 1 and i + 1 <= self._capacity
        return self._reverse[i + 1] != 0

    def get_item(i):
        assert self._contains(i), 'i is invalid!'
        return self._data[i + 1]

    def change(self, i, new_item):
        assert self._contains(i), 'i is invalid!'
        i += 1
        self._data[i] = new_item
        # 找到self._indexes[j] = i, j表示self._data[i]在堆中的位置
        # 之后self._shift_up(j)，再self._shift_down(j) (可以交换顺序)
        # for j in range(self._count + 1):
        #     if self._indexes[j] == i:
        #         self._shift_up(j)
        #         self._shift_down(j)
        #         return
        j = self._reverse[i]
        self._shift_up(j)
        self._shift_down(j)

    def _shift_up(self, index):
        # 因为是最大堆，所以父亲节点的值应该要比孩子节点的值要大的
        while index > 1 and self._data[self._indexes[index // 2]] < self._data[self._indexes[index]]:
            self._data[self._indexes[index // 2]], self._data[self._indexes[index]] = self._data[self._indexes[index]], self._data[self._indexes[index // 2]]
            self._reverse[self._indexes[index // 2]] = index // 2
            self._reverse[self._indexes[index]] = index
            index //= 2

    def _shift_down(self, index):
        while 2 * index <= self._count:
            j = 2 * index # 在此轮循环中，self._data[self._indexes[index]]和self._data[self._indexes[j]]交换位置
            if j + 1 <= self._count and self._data[self._indexes[j + 1]] > self._data[self._indexes[j]]:
                j += 1
            if self._data[self._indexes[index]] >= self._data[self._indexes[j]]:
                break
            self._data[self._indexes[index]], self._data[self._indexes[j]] = self._data[self._indexes[j]], self._data[self._indexes[index]]
            self._reverse[self._indexes[index]] = index
            self._reverse[self._indexes[j]] = j
            index = j


def heap_sort1(arr):
    n = len(arr)
    max_heap = MaxHeap(capacity=n)
    for each in arr:
        max_heap.insert(each)
    for i in range(n - 1, -1, -1):
        arr[i] = max_heap.extract_max()


def heap_sort2(arr):
    max_heap = MaxHeap(arr=arr)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[i] = max_heap.extract_max()


def heap_sort(arr):
    """原地堆排序"""
    n = len(arr)
    for i in range((n - 1) // 2, -1, -1):
        _shift_down(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _shift_down(arr, i, 0)

def _shift_down(arr, n, k):
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j
