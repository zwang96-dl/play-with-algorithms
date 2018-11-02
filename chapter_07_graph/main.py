from chapter_07_graph.sparse_graph import SparseGraph
from chapter_07_graph.dense_graph import DenseGraph
from chapter_07_graph.component import Component
from chapter_07_graph.path import Path
from chapter_07_graph.shortest_path import ShortestPath


if __name__ == '__main__':
    # sparse_graph = SparseGraph(n=3, directed=False)
    # sparse_graph.add_edge(0, 1)
    # sparse_graph.add_edge(0, 2)

    # dense_graph = DenseGraph(n=3, directed=False)
    # dense_graph.add_edge(0, 1)
    # dense_graph.add_edge(0, 2)

    # for vertex in range(len(sparse_graph)):
    #     print('Vertex {} -> {}'.format(
    #         vertex,
    #         ', '.join(str(i) for i in sparse_graph[vertex]),
    #     ))

    # for vertex in range(len(dense_graph)):
    #     print('Vertex {} -> {}'.format(
    #         vertex,
    #         ', '.join(str(i) for i in dense_graph[vertex]),
    #     ))

    # sparse_graph = SparseGraph.from_local_file(
    #     directed=False,
    #     filename='./chapter_07_graph/testG.txt',
    # )
    # print(sparse_graph)

    # dense_graph = DenseGraph.from_local_file(
    #     directed=False,
    #     filename='./chapter_07_graph/testG2.txt',
    # )
    # print(dense_graph)

    # sparse_graph = SparseGraph.from_local_file(
    #     directed=False,
    #     filename='./chapter_07_graph/testG1.txt',
    # )
    # component = Component(sparse_graph)
    # print(component.count())

    # sparse_graph1 = SparseGraph.from_local_file(
    #     directed=False,
    #     filename='./chapter_07_graph/testG1.txt',
    # )
    # component1 = Component(sparse_graph1)
    # print(component1.count())

    # sparse_graph2 = SparseGraph.from_local_file(
    #     directed=False,
    #     filename='./chapter_07_graph/testG2.txt',
    # )
    # component2 = Component(sparse_graph2)
    # print(component2.count())

    # sparse_graph = SparseGraph(n=4, directed=False)
    # sparse_graph.add_edge(0, 1)
    # sparse_graph.add_edge(0, 2)
    # sparse_graph.add_edge(1, 2)
    # component = Component(sparse_graph)
    # print(component.count())

    sparse_graph = SparseGraph.from_local_file(
        directed=False,
        filename='./chapter_07_graph/testG2.txt',
    )
    path = Path(sparse_graph, 0)
    print('DFS: ')
    path.show_path(6)

    sparse_graph_bfs = SparseGraph.from_local_file(
        directed=False,
        filename='./chapter_07_graph/testG2.txt',
    )
    shortest_path = ShortestPath(sparse_graph_bfs, 0)
    print('BFS: ')
    shortest_path.show_path(6)