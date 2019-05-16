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
  @date 2019-05-16 18:20:00
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        status = [[1 for __ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                status[i][j] = status[i-1][j] + status[i][j-1]
        return status[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))