class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool used[9];

        for(int i=0;i<9;i++)
        {
            fill(used,used+9,false);
            for(int j=0;j<9;j++) //检查行
            {
                if(!check(board[i][j],used))
                    return false;
            }

            fill(used,used+9,false);
            for(int j=0;j<9;j++) //检查行
            {
                if(!check(board[j][i],used))
                    return false;
            }
            
        }

        for(int a=0;a<3;a++)
        {
            for(int b=0;b<3;b++)
            {
                fill(used,used+9,false);
                for(int c=a*3;c<a*3+3;c++)
                {
                    for(int d=b*3;d<b*3+3;d++)
                    {
                        if(!check(board[c][d],used))
                            return false;
                    }
                }
            }
        }

        return true;
    }

    
    bool check(char ch,bool used[9])
    {
        if(ch=='.') return true;
        if(used[ch-'1']) return false;
        return used[ch-'1']=true;
    }
    
};