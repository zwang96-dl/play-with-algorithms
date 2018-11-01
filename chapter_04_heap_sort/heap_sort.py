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
                self._sift_down(i)

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def insert(self, item):
        assert (self._count + 1) <= self._capacity, 'heap is full'
        self._data[self._count + 1] = item
        self._count += 1
        self._sift_up(self._count)

    def extract_max(self):
        assert self._count > 0, 'can not extract_max from empty heap'
        ret = self._data[1]
        self._data[1], self._data[self._count] = self._data[self._count], self._data[1]
        self._count -= 1
        self._sift_down(1)
        return ret

    def _sift_up(self, index):
        # 因为是最大堆，所以父亲节点的值应该要比孩子节点的值要大的
        while index > 1 and self._data[index // 2] < self._data[index]:
            self._data[index // 2], self._data[index] = self._data[index], self._data[index // 2]
            index //= 2

    def _sift_down(self, index):
        while 2 * index <= self._count:
            j = 2 * index # 在此轮循环中，self._data[index]和self._data[j]交换位置
            if j + 1 <= self._count and self._data[j + 1] > self._data[j]:
                j += 1
            if self._data[index] >= self._data[j]:
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
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
