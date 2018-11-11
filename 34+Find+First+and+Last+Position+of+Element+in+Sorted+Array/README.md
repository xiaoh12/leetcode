# 题目链接：https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

## 1. 算法
这题重点是需要O(logn)复杂度的算法，否则直接从头至尾遍利一次就可以了。
O(logn)可以先通过二分查找找到target, 再从两边开始向中间找到区间即可。