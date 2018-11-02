class UnionFind1:
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        return self._id[p]

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_id = self._find(p)
        q_id = self._find(q)
        if p_id == q_id:
            return
        for i in range(self._count):
            if self._id[i] == p_id:
                self._id[i] = q_id


class UnionFind2:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        while p != self._parent[p]:
            p = self._parent[p]
        # now p is same value as its parent
        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._parent[p_root] = q_root


class UnionFind3:
    """基于集合数目的优化"""
    def __init__(self, n):
        self._count = n
        # sz[i]表示以i为根的sz集合中的元素
        self._sz = [1] * n
        self._parent = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        while p != self._parent[p]:
            p = self._parent[p]
        # now p is same value as its parent
        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        if self._sz[p_root] < self._sz[q_root]:
            # 小的合并到大的
            self._parent[p_root] = q_root
            self._sz[q_root] += self._sz[p_root]
        else:
            self._parent[q_root] = p_root
            self._sz[p_root] += self._sz[q_root]


class UnionFind4:
    """基于rank优化"""
    def __init__(self, n):
        self._count = n
        # rank[i]表示以i为根的集合所表示的树的层数
        self._rank = [1] * n
        self._parent = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        while p != self._parent[p]:
            p = self._parent[p]
        # now p is same value as its parent
        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        if self._rank[p_root] < self._rank[q_root]:
            # rank小的合并到大的
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1


class UnionFind5:
    """路径压缩"""
    def __init__(self, n):
        self._count = n
        # rank[i]表示以i为根的集合所表示的树的层数
        self._rank = [1] * n
        self._parent = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        while p != self._parent[p]:
            # 路径压缩
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]
        # now p is same value as its parent
        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        if self._rank[p_root] < self._rank[q_root]:
            # rank小的合并到大的
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1


class UnionFind6:
    """路径压缩,递归优化"""
    def __init__(self, n):
        self._count = n
        # rank[i]表示以i为根的集合所表示的树的层数
        self._rank = [1] * n
        self._parent = [i for i in range(n)]

    def _find(self, p):
        assert 0 <= p < self._count
        if p != self._parent[p]:
            # 最终指向了最深的父节点
            self._parent[p] = self._find(self._parent[p])
        return self._parent[p]

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        assert 0 <= p < self._count and 0 <= q < self._count
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        if self._rank[p_root] < self._rank[q_root]:
            # rank小的合并到大的
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1
