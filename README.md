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