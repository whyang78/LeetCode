//方法一：时间复杂度 O(M*N)  空间复杂度 O(M+N)
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        const int m=matrix.size();
        const int n=matrix[0].size();

        vector<bool> rows(m,false);
        vector<bool> columns(n,false);
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(matrix[i][j]==0)
                {
                    rows[i]=true;
                    columns[j]=true;
                }
            }
        }

        for(int i=0;i<m;i++)
        {
            if(rows[i])
            {
                fill(&matrix[i][0],&matrix[i][0]+n,0);
            }
        }

        for(int j=0;j<n;j++)
        {
            if(columns[j])
            {
                for(int i=0;i<m;i++)
                {
                    matrix[i][j]=0;
                }
            }
        }      
    }
};

//方法二：时间复杂度 O(M*N)  空间复杂度 O(1)
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        const int m=matrix.size();
        const int n=matrix[0].size();

        bool row_has_zero=false;
        bool col_has_zero=false;
        for(int j=0;j<n;j++)
        {
            if(matrix[0][j]==0)
            {
                row_has_zero=true;
                break;
            }
        }
        for(int i=0;i<m;i++)
        {
            if(matrix[i][0]==0)
            {
                col_has_zero=true;
                break;
            }
        }

        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                if(matrix[i][j]==0)
                {
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }

        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                if(matrix[i][0]==0||matrix[0][j]==0)
                {
                    matrix[i][j]=0;
                }
            }
        }

        if(row_has_zero)
        {
            for(int j=0;j<n;j++)
            {
                matrix[0][j]=0;
            }
        }

        if(col_has_zero)
        {
            for(int i=0;i<m;i++)
            {
                matrix[i][0]=0;
            }
        }
    }
};