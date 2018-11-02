from chapter_07_graph.sparse_graph import SparseGraph
from chapter_07_graph.dense_graph import DenseGraph


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

    sparse_graph = SparseGraph.from_local_file(
        directed=False,
        filename='./chapter_07_graph/testG.txt',
    )
    print(sparse_graph)

    dense_graph = DenseGraph.from_local_file(
        directed=False,
        filename='./chapter_07_graph/testG.txt',
    )
    print(dense_graph)