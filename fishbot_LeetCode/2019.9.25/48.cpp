//时间：2019-9-25
//作者：fish_bot
//题目：LeetCode 48


//先转置（转置时j=i） 再旋转
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix[0].size();
        
        for(int i = 0; i<n; i++){
            for(int j = i; j<n; j++){
                auto temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = tmp;
      }
    }

    }
};