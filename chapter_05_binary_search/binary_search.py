from collections import deque


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

    def contains(self, key):
        return self._contains(self._root, key)

    def _contains(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else:
            return self._contains(node.right, key)

    def search(self, key):
        return self._search(self._root, key)

    def _search(self, node, key):
        if not node:
            return
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        if node:
            print(node.key)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        self._pre_order(self._root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.key)
            self._in_order(node.right)

    def post_order(self):
        self._post_order(self._root)

    def _post_order(self):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.key)

    def level_order(self):
        queue = deque()
        queue.append(self._root)
        while queue:
            curr = queue.popleft()
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def minimum(self):
        assert self._count > 0
        min_node = self._minimum(self._root)
        return min_node.key

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        assert self._count > 0
        max_node = self._maximum(self._root)
        return max_node.key

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        if self._root:
            self._root = self._remove_min(self._root)

    def _remove_min(self, node):
        if not node.left:
            right_node = node.right
            self._count -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        if self._root:
            self._root = self._remove_max(self._root)

    def _remove_max(self, node):
        if not node.right:
            left_node = node.left
            self._count -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            return
        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:
            if not node.left:
                self._count -= 1
                return node.right
            if not node.right:
                self._count -= 1
                return node.left
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            return successor


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