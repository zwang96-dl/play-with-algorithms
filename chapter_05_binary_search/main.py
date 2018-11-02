from time import time
from chapter_05_binary_search.binary_search import BST


if __name__ == '__main__':
    with open('./chapter_05_binary_search/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time()
    bst = BST()
    for word in words:
        if bst.contains(word):
            bst.search(word).value += 1
        else:
            bst.insert(word, 1)
    print('BST time cost: {} seconds'.format(time() - start_time))
