# 题目链接：https://leetcode.com/problems/linked-list-cycle-ii/description/

## 算法

这题是判断链表是否有环那题的进一步扩展，要找出环的起点。

具体方法还是沿用之前判断是否有环的方法，设定一快一慢两个指针，如果相遇了表示有环，否则快指针会先走到链表结尾。

接下来我们分析一下怎么确定链表的起点：


1. 首先假设链表总长度为L, 如图所示，从head节点至环起点start的距离为a, start点至slow、fast相遇节点meet的距离为b, meet再回到start距离了c。
2. slow走过的总路程为 a + b, fast走过的总路程为 a + b + c + b.
3. slow每次1步，fast每次2步
   
   $$
    (a+b)* 2 = a + b + c + b
   $$
   可以推出
   $$
    a = c
   $$
4. 接着让slow从head开始， fast从meet开始，分别一步一步走，则会在start点相遇，就是我们要求的点



## 类似的扩展
1. 求环的长度
2. 如何解除环
3. 判断两个链表是否相交

有上面的方法稍加改变就可以得到比较好的解。
