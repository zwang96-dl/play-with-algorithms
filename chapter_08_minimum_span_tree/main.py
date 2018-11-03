from chapter_08_minimum_span_tree.dense_graph import DenseGraph
from chapter_08_minimum_span_tree.sparse_graph import SparseGraph
from chapter_08_minimum_span_tree.lazy_prim_mst import LazyPrimMST
from chapter_08_minimum_span_tree.lazy_prim_heap import PrimMST



if __name__ == '__main__':
    # dense_graph = DenseGraph.from_local_file(
    #     directed=True,
    #     filename='./chapter_08_minimum_span_tree/testG1.txt',
    # )
    # print(dense_graph)

    # sparse_graph = SparseGraph.from_local_file(
    #     directed=True,
    #     filename='./chapter_08_minimum_span_tree/testG3.txt',
    # )
    # print(sparse_graph)

    sparse_graph = SparseGraph.from_local_file(
        directed=True,
        filename='./chapter_08_minimum_span_tree/testG1.txt',
    )

    lazy_prime_mst = LazyPrimMST(sparse_graph)
    print('lazy_prime_mst Edges: ', lazy_prime_mst.mst_edges())
    print('lazy_prime_mst Minium weight sum: ', lazy_prime_mst.result())

    prime_mst = PrimMST(sparse_graph)
    print('prime_mst Edges: ', prime_mst.mst_edges())
    print('prime_mst Minium weight sum: ', prime_mst.result())