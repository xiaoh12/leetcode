#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###########################################################################
#
# Copyright (c) 2018 www.codingchen.com, Inc. All Rights Reserved
#
##########################################################################
'''
 @brief leetcode algorithm
 @author chenhui(hui.chen6789@gmail.com)
 @date 2018/11/08 18:43:08
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if len(strs) == 0:
            return prefix
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) - 1 < i or strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix([]))
    print(s.longestCommonPrefix(['aa', 'a']))
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))