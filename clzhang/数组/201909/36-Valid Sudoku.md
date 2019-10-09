## 36 Valid Sudoku

![1569315525307](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1569315525307.png)

![1569315577499](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1569315577499.png)

## Analysis

三个哈希表的容器，长度为9（9行、9列、9块）

vector<unordered_map<int,int>> row(9), col(9), block(9);

每个哈希表存放9个数字是否出现过，遍历81个位置，判断每个位置得数是否在所在的行、列、块出现过，出现过就不满足，return false; 否则将哈希表对应此元素的内容置为1，表示出现过了，下次判断跟它同行、同列或者同块的其他位置的数，若相同就出现过了，false；

所有的位置能遍历完，没有false，就return true

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

