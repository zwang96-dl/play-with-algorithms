from heapq import heappush
from heapq import heappop


class LazyPrimMST:
    def __init__(self, graph):
        self._G = graph
        self._pq = []
        self._marked = [False] * self._G.V()
        self._mst = []
        self._mst_weight = None
        self._visit(0)
        while self._pq:
            e = heappop(self._pq)
            if self._marked[e.v()] == self._marked[e.w()]:
                continue
            self._mst.append(e)
            if not self._marked[e.v()]:
                self._visit(e.v())
            else:
                self._visit(e.w())
        self._mst_weight = self._mst[0].wt()
        for each in self._mst[1:]:
            self._mst_weight += each.wt()

    def mst_edges(self):
        return self._mst

    def result(self):
        return self._mst_weight

    def _visit(self, v):
        assert not self._marked[v]
        self._marked[v] = True
        for e in self._G[v]:
            if not self._marked[e.other(v)]:
                heappush(self._pq, e)