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
 @date 2018/11/08 19:09:33
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
           'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 
        }
        num, i = 0, 0
        while i < len(s):
            if i+1<len(s) and dict_roman[s[i+1]] > dict_roman[s[i]]:
                num += dict_roman[s[i+1]]-dict_roman[s[i]]
                i +=2
            else :
                num += dict_roman[s[i]]
                i +=1
        return num  


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('III'))