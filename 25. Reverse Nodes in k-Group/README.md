## 题目链接：https://leetcode.com/problems/reverse-nodes-in-k-group/description/

## 算法
这题是第24题Swap Nodes in Pairs的升级版。
需要注意的是，在处理了K个结点反转之后，要额外处理一下head和tail. 所以需要保存在反转K之前的head和之后的tail.
详细逻辑见代码，已加上注释.


## 另一个解法
和上一个解法略有不同，只是反转K个子链表的时候，用了一个deque, 空间不满足要求。
```
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # helper deque
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        deque = []
        while cur:
            deque.append(cur)
            cur = cur.next
            if len(deque) == k:
                while deque:
                    pre.next = deque.pop()
                    pre = pre.next
        # if total_len % k
        while deque:
            pre.next = deque.pop(0)
            pre = pre.next
        # tail must be None
        pre.next = None
        return dummy.next
```