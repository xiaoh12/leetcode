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
  @date 2018-11-29 14:18:08
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while not slow is fast:
            slow = slow.next
            fast = fast.next
        return slow