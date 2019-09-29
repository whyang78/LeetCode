//分发糖果

//方法一：暴力求解
//分别从左至右、从右至左遍历rating,不断更新candy数组，直至数组不再发生变化，最后统计总数
//时间复杂度：O(N2)  空间复杂度：O(N)
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty())
            return 0;

        int sum=0;
        vector<int> candy(ratings.size(),1);
        bool change=true;

        while(change)
        {
            change=false;
            for(int i=1;i<ratings.size();i++)
            {
                if(ratings[i]>ratings[i-1] && candy[i]<=candy[i-1])
                {
                    candy[i]=candy[i-1]+1;
                    change=true;
                }
            }

            for(int i=ratings.size()-2;i>=0;i--)
            {
                if(ratings[i]>ratings[i+1] && candy[i]<=candy[i+1])
                {
                    candy[i]=candy[i+1]+1;
                    change=true;
                }
            }
        }

        sum=accumulate(candy.begin(),candy.end(),0);
        return sum;
    }
};


//方法二：设两个数组
//分别更新一下两个数组，取相应位置的最大值为最终结果，最后统计总数
//时间复杂度：O(N)  空间复杂度：O(N)
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty())
            return 0;

        int sum=0;
        vector<int> left2right(ratings.size(),1);
        vector<int> right2left(ratings.size(),1);
 
        for(int i=1;i<ratings.size();i++)
        {
            if(ratings[i]>ratings[i-1])
            {
                left2right[i]=left2right[i-1]+1;
            }
        }

        for(int i=ratings.size()-2;i>=0;i--)
        {
            if(ratings[i]>ratings[i+1])
            {
                right2left[i]=right2left[i+1]+1;
            }
        }
        
        for(int i=0;i<ratings.size();i++)
        {
            sum+=max(left2right[i],right2left[i]);
        }
        
        return sum;
    }
};


//方法三：使用一个数组
//时间复杂度：O(N)  空间复杂度：O(N)
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty())
            return 0;

        int sum=0;
        vector<int> candy(ratings.size(),1);
 
        for(int i=1;i<ratings.size();i++)
        {
            if(ratings[i]>ratings[i-1])
            {
                candy[i]=candy[i-1]+1;
            }
        }

        for(int i=ratings.size()-2;i>=0;i--)
        {
            if(ratings[i]>ratings[i+1])
            {
                candy[i]=max(candy[i],candy[i+1]+1);
            }
        }

        sum=accumulate(candy.begin(),candy.end(),0);

        return sum;
    }
};

//方法三：使用一个数组
//时间复杂度：O(N)  空间复杂度：O(N)
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty())
            return 0;

        int sum=0;
        vector<int> candy(ratings.size(),1);
 
        for(int i=1;i<ratings.size();i++)
        {
            if(ratings[i]>ratings[i-1])
            {
                candy[i]=candy[i-1]+1;
            }
        }

        for(int i=ratings.size()-2;i>=0;i--)
        {
            if(ratings[i]>ratings[i+1])
            {
                candy[i]=max(candy[i],candy[i+1]+1);
            }
        }

        sum=accumulate(candy.begin(),candy.end(),0);

        return sum;
    }
};


//方法四：遍历一次
//时间复杂度：O(N)  空间复杂度：O(1)
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty())
            return 0;

        int sum=0;
        int cursum=1;
 
        for(int i=0;i<ratings.size()-1;)
        {
            if(ratings[i]==ratings[i+1])
            {
                sum+=cursum;
                i++;
                cursum=1;
            }
            else if(ratings[i]<ratings[i+1])
            {
                for(;i<ratings.size()-1 && ratings[i]<ratings[i+1];i++) sum+=(cursum++);
            }
            else if(ratings[i]>ratings[i+1])
            {
                int decount=1;
                for(;i<ratings.size()-1 && ratings[i]>ratings[i+1];i++) sum+=(decount++);
                sum+=max(cursum,decount);
                sum--;
                cursum=1;
            }
        }
        sum+=cursum;

        return sum;
    }
};