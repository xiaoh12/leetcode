## 题目链接：https://leetcode.com/problems/valid-parentheses/description/

## 算法
很典型的堆栈问题。

把左括号依次入栈，当遇到右括号时，弹出栈顶的元素进行比较，看是否匹配。

这题在体现Python代码优势上有两点可以表现一下：
1. 第一是下面这个match_dict的写法，这让后面在判断括号是否匹配上，不需要用```if else```了
```
match_dict = {')':'(', ']':'[', '}':'{'}
```
2. 第二是最后return的地方,按最简单直接的思考方式,判断stack是否为空，空则返回True,否则返回False：
```
if len(stack) == 0:
    return True
else:
    return False
```
但用```return not stack```就优雅多了
