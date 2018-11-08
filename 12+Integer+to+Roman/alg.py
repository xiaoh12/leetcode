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
 @date 2018/11/08 19:09:33
'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        simbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        i = 0
        while num > 0:
            number = num % 10
            if number < 4:
                roman = ''.join([simbols[2*i] for _ in range(number)]) + roman
            elif number == 4:
                roman = simbols[2*i] + simbols[2*i+1] + roman
            elif number > 4 and number < 9:
                roman = simbols[2*i+1] + ''.join([simbols[2*i] for _ in range(number - 5)]) + roman 
            elif number == 9:
                roman = simbols[2*i] + simbols[2*i+2] + roman
            num = num // 10
            i += 1
        return roman
   

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))


    