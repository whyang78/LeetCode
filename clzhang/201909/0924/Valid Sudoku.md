## Question: Valid Sudoku

![1569315525307](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1569315525307.png)

![1569315577499](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1569315577499.png)

## Analysis

0

```c++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_map<int,int>> row(9), col(9), block(9);
        for(int i = 0; i < 9; ++ i){
            for(int j = 0; j < 9; ++ j){
                int bindex =  (i / 3)* 3 + j / 3;
                char cur = board[i][j];
                if(cur == '.')  continue;
                if(row[i].count(cur) || col[j].count(cur) || block[bindex].count(cur))  return false;
                row[i][cur] = 1;
                col[j][cur] = 1;
                block[bindex][cur] = 1;
            }
        }
        return true;
    }
};
```

