class Component:
    """Only for dense graph"""
    def __init__(self, graph):
        self._graph = graph
        self._visited = [False] * graph.V()
        self._ccount = 0
        self._id = [-1] * graph.V()
        for i in range(graph.V()):
            if not self._visited[i]:
                self._dfs(i)
                self._ccount += 1

    def count(self):
        return self._ccount

    def _dfs(self, v):
        self._visited[v] = True
        self._id[v] = self._ccount
        for i in self._graph[v]:
            if not self._visited[i]:
                self._dfs(i)

    def is_connected(self, v, w):
        assert 0 <= v < self._graph.V()
        assert 0 <= w < self._graph.V()
        return self._id[v] == self._id[w]