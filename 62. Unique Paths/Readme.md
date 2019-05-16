## 心得
比较简单的动态规划题目。
存好状态数组并处理好边界条件就可以得出正确解

## 学习
从题目的discuss里看到一个提升，我的算法里用了二维list存状态，其实可以只用一维。
看下面的代码可以发现，先按m初始化好值为1的数组，然后从n维开始做外层循环，因为前一次计算完的结果在后面不会再用到了，所以可以直接覆盖，节约了空间。
下图是m = 4, n =3的情况，计算的过程就是从左到右生成下面这个，每一列就是要存的arr.

1 1 1

1 2 3

1 3 6

1 4 10

```
public class Solution {
    public int uniquePaths(int m, int n) {
        int[] arr = new int[m];
        for (int i = 0; i < m; i++) {
            arr[i] = 1;
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                arr[j] = arr[j] + arr[j-1];
            }
        }
        return arr[m-1];
    }
}
```