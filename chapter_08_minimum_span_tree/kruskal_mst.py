from chapter_06_union_find.union_find import UnionFind6 as UnionFind
from chapter_04_heap_sort.heap_sort import MinHeap


class KruskalMST:
    def __init__(self, graph):
        self._mst = []
        pq = MinHeap(capacity=graph.E())
        for i in range(graph.V()):
            for e in graph[i]:
                if e.v() <= e.w():
                    pq.insert(e)
        uf = UnionFind(graph.V())
        while not pq.is_empty() and len(self._mst) < graph.V() - 1:
            e = pq.extract_min()
            if uf.is_connected(e.v(), e.w()):
                continue
            self._mst.append(e)
            uf.union(e.v(), e.w())
        self._mst_weight = self._mst[0].wt()
        for each in self._mst[1:]:
            self._mst_weight += each.wt()

    def mst_edges(self):
        return self._mst

    def result(self):
        return self._mst_weight