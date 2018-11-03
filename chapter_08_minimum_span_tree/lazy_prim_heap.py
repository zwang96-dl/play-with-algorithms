from chapter_04_heap_sort.heap_sort import IndexMinHeap


class PrimMST:
    def __init__(self, graph):
        self._G = graph
        assert self._G.E() >= 1
        self._ipq = IndexMinHeap(capacity=graph.V())
        self._marked = [False] * self._G.V()
        self._edge_to = [None] * self._G.V()
        self._mst = []
        self._visit(0)
        while not self._ipq.is_empty():
            v = self._ipq.extract_min_index()
            assert self._edge_to[v] is not None
            self._mst.append(self._edge_to[v])
            self._visit(v)
        self._mst_weight = self._mst[0].wt()
        for each in self._mst[1:]:
            self._mst_weight += each.wt()

    def _visit(self, v):
        assert not self._marked[v]
        self._marked[v] = True
        for e in self._G[v]:
            w = e.other(v)
            if not self._marked[w]:
                if not self._edge_to[w]:
                    self._edge_to[w] = e
                    self._ipq.insert(w, e.wt())
                elif e.wt() < self._edge_to[w].wt():
                    self._edge_to[w] = e
                    self._ipq.change(w, e.wt())

    def mst_edges(self):
        return self._mst

    def result(self):
        return self._mst_weight