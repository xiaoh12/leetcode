# 题目链接：https://leetcode.com/problems/integer-to-roman/description/
## 1. 算法
这题挺简单，把0~9区分成0<x<4, 4, 4<x<9, 9这4部份，再用```if else```实现就可以了.

看了一下网上其它人的解法，好像我的还高级一点，比如他们直接枚举了，虽然也解了。
```
M = ["", "M", "MM", "MMM"];
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
```