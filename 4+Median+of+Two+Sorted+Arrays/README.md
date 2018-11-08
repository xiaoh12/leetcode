# 题目链接：https://leetcode.com/problems/median-of-two-sorted-arrays/description/

## 1. 算法

简单实现归并排序后，根据总数是奇数或偶数来决定中位数是一个还是两个。

我的算法没有完全把两个数组全部归并排完，因为题中有说明nums1和nums2是已排好序的，所以我只归并了前一半的数据。
