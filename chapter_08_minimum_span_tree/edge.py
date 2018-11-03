class Edge:
    def __init__(self, a=None, b=None, weight=None):
        # 从a指向b
        self._a = a
        self._b = b
        self._weight = weight

    def v(self):
        return self._a

    def w(self):
        return self._b

    def wt(self):
        return self._weight

    def other(self, x):
        assert x == self._a or x == self._b
        return self._b if x == self._a else self._a

    def __str__(self):
        return '{} -> {}'.format(self._a, self._b)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other_edge):
        assert isinstance(other_edge, Edge), 'can not other type with <Edge> object'
        return self._weight < other_edge.wt()

    def __le__(self, other_edge):
        assert isinstance(other_edge, Edge), 'can not other type with <Edge> object'
        return self._weight <= other_edge.wt()

    def __gt__(self, other_edge):
        assert isinstance(other_edge, Edge), 'can not other type with <Edge> object'
        return self._weight > other_edge.wt()

    def __ge__(self, other_edge):
        assert isinstance(other_edge, Edge), 'can not other type with <Edge> object'
        return self._weight >= other_edge.wt()


