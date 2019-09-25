//时间：2019-9-19
//作者：fish_bot
//题目：LeetCode 15

//先排序，后两端指针逼近
//跳过重复的

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        vector<vector<int>> result;
        
        if (nums.size() < 3) return result;
        
        sort(nums.begin(),nums.end());

        int len = nums.size();
        int i,j,k;
        for(k = 0; k < len - 2; k++)
        {
            if(nums[k]>0)
        	    break;
            if(k>0 && nums[k]==nums[k-1])
                continue;
            i = len - 1;
            j = k + 1;
            while(j < i)
            {
                if(nums[i]+nums[j]+nums[k]>0)
                    i--;
                else if(nums[i]+nums[j]+nums[k]<0)
                    j++;
                else
                {
                    result.push_back({nums[k],nums[j],nums[i]});
                    
                    while(i>j&&nums[i]==nums[i-1])      
        			    i--;
        			while(i>j&&nums[j]==nums[j+1])      
        			    j++;
        			i--;
        			j++;
                }
            }
        }
        return result;
    }
};