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
 @date 2018/11/06 22:30:33
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = int(str(abs(x))[::-1])
        if x < 0:
            y *= -1
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y

    def reverse_other(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        flag_neg = 0
        if x < 0:
            # python负数除法默认是向下取整,先计算正值最后再乘-1
            flag_neg = 1
            x = -1 * x
        while x != 0:
            pop = x % 10
            x = x // 10 
            y = y * 10 + pop
            if y > 2**31-1 or y < -2**31:
                return 0
        if flag_neg == 1:
            y = -1 * y
        return y

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse_other(-345))
    print(s.reverse(1534236469))
