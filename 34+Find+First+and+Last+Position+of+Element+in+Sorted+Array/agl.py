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
 @date 2018/11/11 15:25:41
'''

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                while nums[low] != target:
                    low += 1
                while nums[high] != target:
                    high -= 1
                return [low, high]
        return [-1, -1]

            


    def searchRange_liner_scan(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = end = -1
        for i in range(len(nums)):
            if target == nums[i] and start == -1:
                start = i
                end = i
            if target == nums[i] and start != -1:
                end = i
            if target < nums[i]:
                break
        return [start, end]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([2, 2], 2))
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))
    print(s.searchRange([1], 1))
    




''' vim: set expandtab ts=4 sw=4 sts=4 tw=100: '''
