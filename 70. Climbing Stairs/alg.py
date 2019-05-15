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
  @date 2019-05-15 15:30:21
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        status = [0 for _ in range(0, n+1)]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            status[1] = 1
            status[2] = 2
            for i in range(3, n+1):
                status[i] = status[i-1] + status[i-2]
        return status[n]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))