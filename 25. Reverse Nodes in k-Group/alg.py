#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###########################################################################
#
# Copyright (c) 2018 www.codingchen.com, Inc. All Rights Reserved
#
##########################################################################
'''
  @brief leetcode algorithm
  @author chenhui
  @date 2018-11-29 16:34:13
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        # save first k node's head in dummy
        dummy = ListNode(-1)
        dummy.next = head
        run = dummy
        while run:
            temp = run
            for i in range(k):
                if not temp.next:
                    return dummy.next
                temp = temp.next
            # reverse k nodes
            node = run.next
            pre = run
            cur = run.next
            for i in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            # connect head and tail
            node.next, run.next, run = cur, pre, node
        return dummy.next