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
 @date 2018/11/12 22:50:25
'''

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = '0'
        start_flag = False
        symbol_flag = 1
        for i in range(len(str)):
            if str[i] == ' ' and start_flag == False:
                continue
            elif str[i] == '-' and start_flag == False:
                symbol_flag = -1
                start_flag = True
            elif str[i] == '+' and start_flag == False:
                symbol_flag = 1
                start_flag = True
            elif str[i].isdigit():
                start_flag = True
                num = num + str[i]
            elif str[i].isalpha():
                break
            else:
                break
        num = int(num) * symbol_flag
        if num > 2**31 -1:
            num = 2**31 -1
        if num < -2**31:
            num = -2**31
        return num

        
if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('-'))
    print(s.myAtoi('+1'))
    print(s.myAtoi('+-2'))
    print(s.myAtoi('42'))
    print(s.myAtoi('    -42'))
    print(s.myAtoi('4193 with words'))
    print(s.myAtoi('words and 987'))
    print(s.myAtoi('-91283472332'))