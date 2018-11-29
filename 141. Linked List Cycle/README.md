# 题目链接：https://leetcode.com/problems/linked-list-cycle/description/

## 算法
两个指针slow、fast, 判断链表里是否有环，则让slow一次走一步，fast一次走两步，如果slow、fast后面相遇了，那就存在环，否则就不存在环。

算法的时间复杂度是O(n)

在看其它解法的时候把代码做了个小改进：
```
    while slow and fast and fast.next:

    while fast and fast.next:
```
去掉了slow, 因为slow一直是跑的比fast要慢，这样提交有时能到40ms
