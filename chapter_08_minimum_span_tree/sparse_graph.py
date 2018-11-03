from chapter_08_minimum_span_tree.edge import Edge


class SparseGraph:
    def __init__(self, n, directed):
        self._n = n
        self._m = 0
        self._directed = directed
        self._g = [[] for _ in range(n)]

    def V(self):
        return self._n

    def E(self):
        return self._m

    def add_edge(self, v, w, weight):
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        self._g[v].append(Edge(v, w, weight))
        if v != w and not self._directed:
            self._g[w].append(Edge(w, v, weight))
        self._m += 1

    def has_edge(self, v, w):
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        for i in range(len(self._g[v])):
            if self._g[v][i].other(v) == w:
                return True
        return False

    def __iter__(self):
        """`i for i in sparse_graph_obj`"""
        yield from self._g

    def __len__(self):
        return self._n

    def __getitem__(self, v):
        assert 0 <= v < self._n
        return self._g[v]

    def __str__(self):
        ret = ['<chapter_08_minimum_span_tree.sparse_graph.SparseGraph object>:']
        for v in range(len(self._g)):
            temp = []
            for each_edge in self._g[v]:
                temp.append(' to {} with weight {:1.4f}'.format(each_edge.w(), each_edge.wt()).rjust(8))
            ret.append('vertex {}: '.format(v).rjust(4) + ', '.join(temp))
        return '\n'.join(ret)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_local_file(cls, directed, filename):
        with open(filename, 'r') as f:
            rows = f.read()
        rows = rows.split('\n')
        data = [each_row_str.split() for each_row_str in rows]
        n, _ = data[0]
        n = int(n)
        data = data[1:]
        graph = cls(n=n, directed=directed)
        for each_row in data:
            from_edge, end_edge, weight = each_row
            graph.add_edge(int(from_edge), int(end_edge), float(weight))
        return graph