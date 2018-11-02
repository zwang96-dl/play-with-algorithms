from sort_test_helper.helpers import union_find_test_helper
from chapter_06_union_find.union_find import UnionFind1
from chapter_06_union_find.union_find import UnionFind2
from chapter_06_union_find.union_find import UnionFind3
from chapter_06_union_find.union_find import UnionFind4
from chapter_06_union_find.union_find import UnionFind5
from chapter_06_union_find.union_find import UnionFind6


if __name__ == '__main__':
    n = 10000

    # uf1 = UnionFind1(n)
    # uf2 = UnionFind2(n)
    uf3 = UnionFind3(n)
    uf4 = UnionFind4(n)
    uf5 = UnionFind5(n)
    uf6 = UnionFind6(n)
    # union_find_test_helper(uf1, n, 'First Version UF')
    # union_find_test_helper(uf2, n, 'Second Version UF')
    union_find_test_helper(uf3, n, 'Third Version UF')
    union_find_test_helper(uf4, n, 'Fourth Version UF')
    union_find_test_helper(uf5, n, 'Fifth Version UF')
    union_find_test_helper(uf6, n, 'Sixth Version UF')
