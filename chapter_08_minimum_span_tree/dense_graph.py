from chapter_08_minimum_span_tree.edge import Edge


class DenseGraph:
    def __init__(self, n, directed):
        # n表示图的节点数
        self._n = n
        # m表示图的边数
        self._m = 0
        self._directed = directed
        self._g = [[None] * n for _ in range(n)]

    def V(self):
        return self._n

    def E(self):
        return self._m

    def add_edge(self, v, w, weight):
        """顶点v和顶点w连接"""
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        if not self.has_edge(v, w):
            self._m += 1
        self._g[v][w] = Edge(v, w, weight)
        if not self._directed:
            self._g[w][v] = Edge(w, v, weight)
        

    def has_edge(self, v, w):
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        return self._g[v][w] != None

    def __iter__(self):
        """`i for i in dense_graph_obj`"""
        yield from self._g

    def __len__(self):
        return self._n

    def __getitem__(self, v):
        assert 0 <= v < self._n
        return self._g[v]

    def __str__(self):
        ret = ['<chapter_08_minimum_span_tree.dense_graph.DenseGraph object>:']
        header_gutter = 8
        header = ''.rjust(header_gutter) + ''.join(str(i).rjust(header_gutter) for i in range(len(self._g)))
        ret.append(header)
        for v in range(len(self._g)):
            temp = ''
            for each_edge in self._g[v]:
                if each_edge is None:
                    temp += ''.rjust(8)
                else:
                    temp += ' {:1.4f}'.format(each_edge.wt()).rjust(8)
            ret.append('vertex {}: '.format(v) + temp)
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