## play-with-data-structures

Python implementation of imooc course [玩转数据结构](https://coding.imooc.com/class/207.html), thanks for that great course (instructor [liuyubobobo](https://github.com/liuyubobobo)) !

Any pull-request is welcome:)

Any quesitons please email to wangzhe.dut@gmail.com


### Some course notes

1. 选择排序
- 从当前未排序的序列中选择最小的值


2. 插入排序
- 将当前处理的元素插入到前面排好的位置上，对于近乎有序的数组复杂度为O(n), can be used for shell sort.


3. 冒泡排序
- move the largest element to the end of the array everytime


4. Merge sort
- 需要O(n)的空间复杂度
- 小数据使用insertion_sort
- 也可以自底向上归并排序, 可以在nlog(n)时间内对链表进行排序（因为不需要用到数组索引）!!!


5. 快速排序
- 对近乎有序的数组排序效率很差，退化成O(n^2)。解决方案：随机化选择pivot
- 对重复元素多的数组排序效率很差。解决方案：双路（三路）快排
- 双路排序是分出了大于和小于pivot_value的两部分，三路排序是加上了等于pivot_value的部分


6. Heap sort
- shift up
- shift down
- heapify 所有的叶子节点可以看成是最大堆，第一个非叶子节点是最后一个叶子节点的index除以2（index // 2），对每一个非叶子节点（反向）进行shift_down即可
- 一个个插入空堆，时间复杂度是O(nlogn)，heapify是O(n) !!!! 因为上来就抛弃了近乎一半的叶子节点
- 可以原地堆排序优化（空间优化），空间复杂度O(1)
- 现将最大的值放在数组最后一个位置，再与第一个位置交换并shift_down
- 快排额外空间是O(logn)
- 插入，归并是稳定排序；快排和堆排是不稳定排序，可以自定义比较函数，让排序算法不存在稳定性问题。
- 索引堆（Index Heap）新建一个索引数组，不用移动原始数组，而改变索引数组即可（典型的空间换时间策略），适合于复杂元素数组（move cost比较大的）
- 应用场景：动态优先级的情况
- 多路归并排序: 比如4路，每次将4个元素推入堆中，n路归并退化成堆排序
- d叉堆(d-ary heap)：每个元素可以有3个孩子
- 思路：最大最小队列（同时维护一个最大堆和一个最小堆）
- 二项堆，斐波那契堆


7. 二分查找
- 对于有序的数列才能使用二分查找
- floor and ceil


8. 并查集
- 解决的是连接问题（而不是路径问题），少了很多信息，因此可以更高效的回答。
- 并查集的操作时间复杂度近乎是O(1)的


9. Graph
- 无向图（Undirected Graph）
- 有向图（Directed Graph）
- 无权图（Unweighted Graph）
- 有权图（Weighted Graph）
- 图的连通性（图中的点不一定都是连在一起的）
- 自环边（self-loop）
- 平行边（parallel-edges）
- 简单图（没有自环边和平行边）
- 图的表示：邻接矩阵（Adjacency Matrix，适合稠密图）,邻接表（Adjacency Lists，适合稀疏图）
- DFS -> 稀疏图（邻接表）：O(V+E)
- DFS -> 稠密图（邻接矩阵）：O(V^2)
- 广度优先：在加入队列之前时刻判断是否应该加入队列，可以用来找最短距离，先遍历到的点的距离一定小于等于后遍历到的点的距离
- 广度优先复杂度和深度优先的复杂度一致
- flood fill算法（PS抠图）
- 二分图(买方，卖方，路径是达成交易的价格)