from chapter_08_minimum_span_tree.sparse_graph import SparseGraph
from chapter_09_shortest_path.dijkstra import Dijkstra
from chapter_09_shortest_path.bellman_ford import BellmanFord



if __name__ == '__main__':
    sparse_graph = SparseGraph.from_local_file(
        directed=True,
        filename='./chapter_09_shortest_path/testG1.txt',
    )
    dij = Dijkstra(sparse_graph, 0)

    print('Dijkstra: ')
    for w in range(5):
        dij.show_path(w)

    sparse_graph2 = SparseGraph.from_local_file(
        directed=True,
        filename='./chapter_09_shortest_path/testG2.txt',
    )
    bell = BellmanFord(sparse_graph2, 0)
    print('Bellman-Ford: ')
    if bell.negative_cycle():
        print('The graph contains gegative cycle!')
    else:
        for w in range(5):
            bell.show_path(w)