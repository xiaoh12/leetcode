#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###########################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
##########################################################################
'''
 @brief leetcode algorithm
 @author chenhui(hui.chen6789@gmail.com)
 @date 2018/11/10 15:55:08
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 7))