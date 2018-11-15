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
 @date 2018-11-14 22:35:52
'''

class Solution:    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        self.backtrack('', arr, n, n)
        return arr

    def backtrack(self, s, arr, left, right):
        if (left == 0 and right == 0):
            arr.append(s)
        if left > right:
            return
        if left > 0:
            self.backtrack(s+'(', arr, left-1, right)
        if right > 0:
            self.backtrack(s+')', arr, left, right-1)

    def generateParenthesis_loop(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        left, right = [], []
        for _ in range(n*2):
            if len(result) == 0:
                result.append('(')
                left.append(1)
                right.append(0)
            for i in range(len(result)):
                if (left[i] - right[i]) == 0 and left[i] < n:
                    result[i] += '('
                    left[i] += 1
                elif (left[i] - right[i]) > 0 and left[i] < n:
                    result.append(result[i]+')')
                    left.append(left[i])
                    right.append(right[i]+1)
                    result[i] += '('
                    left[i] += 1
                elif left[i] == n and right[i] < n:
                    result[i] += ')'
                    right[i] += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))