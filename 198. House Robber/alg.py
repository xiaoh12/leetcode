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
  @date 2019-01-02 18:06:17
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cash = [0 for _ in range(len(nums))]
        cash[0] = nums[0]
        cash[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cash[i] = max(cash[i-1], cash[i-2]+nums[i])
        return cash[-1]

if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    s = Solution()
    print(s.rob(nums))