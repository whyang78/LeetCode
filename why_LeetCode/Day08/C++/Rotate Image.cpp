//个人理解：沿（副）对角线变化，角度变化是180°；
//沿竖（横）中线变化，角度变化是90°
//两种解法：副对角线+横中线  对角线（转置）+竖中线

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int n=matrix.size();
        
        // 沿着副对角线反转
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n-i;j++)
            {
                swap(matrix[i][j],matrix[n-1-j][n-1-i]);
            }
        }

        //沿横中线反转
        for(int i=0;i<n/2;i++)
        {
            for(int j=0;j<n;j++)
            {
                swap(matrix[i][j],matrix[n-1-i][j]);
            }
        }   
    }
};