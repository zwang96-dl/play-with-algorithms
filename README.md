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