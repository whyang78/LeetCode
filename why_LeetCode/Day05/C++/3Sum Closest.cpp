'''
œ»≈≈–Ú£¨»ª∫Û◊Û”“º–±∆£¨∏¥‘”∂»O(n2)

'''

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int result=0;
        int min_gap=INT_MAX;
        sort(nums.begin(),nums.end());
        
        auto begin=nums.begin(),last=nums.end()-1;
        for(auto i=begin;i!=prev(last,1);i++)
        {
            auto j=next(i);
            auto k=last;
            while(j<k)
            {
                const int sum=*(i)+*(j)+*(k);
                const int gap=abs(sum-target);
                if(gap<min_gap)
                {
                    result=sum;
                    min_gap=gap;
                }
                if(sum<target) 
                    j++;
                else if(sum>target)
                    k--;
                else
                    return sum;
            }
        }
        return result;
    }
};