class BST:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = self.right = None

    def __init__(self):
        self._root = None
        self._count = 0

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return self._Node(key, value)
        if node.key == key:
            node.value = value
            return node
        elif node.key > key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        return node


def binary_search(arr, target):
    # 在arr[l...r]之中查找target
    # 二分的核心思想是排除不符合条件的那一半
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1