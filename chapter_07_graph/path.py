class Path:
    def __init__(self, graph, s):
        self._G = graph
        assert 0 <= s < self._G.V()
        # s是从哪里起步
        self._s = s
        self._from = [-1] * self._G.V()
        self._visited = [False] * self._G.V()
        self._dfs(s)

    def has_path(self, w):
        """从s到w有没有路径"""
        assert 0 <= w < self._G.V()
        return self._visited[w]

    def path(self, w):
        """从s到w点的路径"""
        assert 0 <= w < self._G.V()
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self._from[p]
        return s

    def show_path(self, w):
        """打印从s到w点的路径"""
        vec = self.path(w)
        print('start ' +  ' -> '.join(str(i) for i in vec[::-1]) + ' end')

    def _dfs(self, v):
        self._visited[v] = True
        for i in self._G[v]:
            if not self._visited[i]:
                self._from[i] = v
                self._dfs(i)
