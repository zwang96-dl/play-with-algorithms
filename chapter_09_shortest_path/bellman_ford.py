from chapter_08_minimum_span_tree.edge import Edge


class BellmanFord:
    def __init__(self, graph, s):
        self._G = graph
        self._s = s
        self._dist_to = [0] * self._G.V()
        self._from = [None] * self._G.V()
        self._has_negative_cycle = False
        # Bellman-Ford
        self._dist_to[self._s] = 0
        self._from[s] = Edge(self._s, self._s, 0)
        for index in range(1, self._G.V()):
            # relaxation
            for i in range(self._G.V()):
                for e in self._G[i]:
                    if self._dist_to[e.v()] + e.wt() < self._dist_to[e.w()] or \
                        not self._from[e.w()]:
                        self._dist_to[e.w()] = self._dist_to[e.v()] + e.wt()
                        self._from[e.w()] = e
        self._has_negative_cycle = self._detect_negative_cycle()

    def _detect_negative_cycle(self):
        for i in range(self._G.V()):
            for e in self._G[i]:
                if self._dist_to[e.v()] + e.wt() < self._dist_to[e.w()] or \
                    not self._from[e.w()]:
                    return True
        return False

    def negative_cycle(self):
        return self._has_negative_cycle

    def shortest_path_to(self, w):
        assert 0 <= w < self._G.V()
        assert not self._has_negative_cycle
        assert self.has_path_to(w)
        return self._dist_to[w]

    def has_path_to(self, w):
        assert 0 <= w < self._G.V()
        return self._from[w] is not None

    def shortest_path(self, w):
        assert 0 <= w < self._G.V()
        assert not self._has_negative_cycle
        assert self.has_path_to(w)
        s = []
        e = self._from[w]
        while e.v() != self._s:
            s.append(e)
            e = self._from[e.v()]
        s.append(e)
        return s[::-1]

    def show_path(self, w):
        assert 0 <= w < self._G.V()
        assert not self._has_negative_cycle
        assert self.has_path_to(w)
        vec = self.shortest_path(w)
        print('Shortest path from {} to {}: {}'.format(
            self._s,
            w,
            '{} -> '.format(self._s) + ' -> '.join(str(i.w()) for i in vec))
        )