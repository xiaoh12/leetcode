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
  @date 2018-12-03 11:38:03
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match_dict = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in match_dict.keys():
                stack.append(c)
            else:
                if not stack or not match_dict[c] is stack.pop():
                    return False
        return not stack