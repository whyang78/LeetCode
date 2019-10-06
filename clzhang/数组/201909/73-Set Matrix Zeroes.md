## 73 Set Matrix Zeroes （矩阵置零）

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

**示例 1:**

```
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

## A

遍历M*N，记录要删的行、列，需要额外的空间：
$$
\mathcal{O}（M + N）
$$
时间复杂度：
$$
\mathcal{O}(MN)
$$


```C++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0) return;
        int M = matrix.size() - 1;      //row
        int N = matrix[0].size() - 1;   //col
        
        // cout << M+1 << N+1;
        vector<int> row(M+1, 0);
        vector<int> col(N+1, 0);
        for (int i = 0; i <= M; i++) {  //记录要删的行、列，额外的空间：（M + N）
            for (int j = 0; j <= N; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }
        for (int i = 0; i <= M; i++) {
            if (row[i]){
                for(int j = 0; j <= N; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int j = 0; j <= N; j++) {
            if (col[j]) {
                for (int i = 0; i <= M; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};
```

