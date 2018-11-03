from chapter_04_heap_sort.heap_sort import IndexMinHeap
from chapter_08_minimum_span_tree.edge import Edge


class Dijkstra:
    def __init__(self, graph, s):
        self._G = graph
        assert 0 <= s < self._G.V()
        self._s = s
        self._dist_to = [0] * self._G.V()
        self._marked = [False] * self._G.V()
        self._from = [None] * self._G.V()
        self._ipq = IndexMinHeap(self._G.V())
        self._dist_to[s] = 0
        self._from[s] = Edge(s, s, 0)
        self._ipq.insert(s, self._dist_to[s])
        self._marked[s] = True
        while not self._ipq.is_empty():
            v = self._ipq.extract_min_index()
            self._marked[v] = True
            for e in self._G[v]:
                w = e.other(v)
                if not self._marked[w]:
                    if not self._from[w] or self._dist_to[v] + e.wt() < self._dist_to[w]:
                        self._dist_to[w] = self._dist_to[v] + e.wt()
                        self._from[w] = e
                        if self._ipq._contains(w):
                            self._ipq.change(w, self._dist_to[w])
                        else:
                            self._ipq.insert(w, self._dist_to[w])

    def shortest_path_to(self, w):
        assert 0 <= w < self._G.V()
        assert self.has_path_to(w)
        return self._dist_to[w]

    def has_path_to(self, w):
        assert 0 <= w < self._G.V()
        return self._marked[w]

    def shortest_path(self, w):
        assert 0 <= w < self._G.V()
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
        assert self.has_path_to(w)
        vec = self.shortest_path(w)
        print('Shortest path from {} to {}: {}'.format(
            self._s,
            w,
            '{} -> '.format(self._s) + ' -> '.join(str(i.w()) for i in vec))
        )