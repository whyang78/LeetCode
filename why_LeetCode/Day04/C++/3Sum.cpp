'''
首先对原数组进行排序，然后开始遍历排序后的数组，
这里注意不是遍历到最后一个停止，而是到倒数第三个就可以了，
中间如果遇到跟前一个数相同的数字就直接跳过。
对于遍历到的数，如果大于0则跳到下一个数，因为三个大于0的数相加不可能等于0；
否则用0减去这个数得到一个sum，我们只需要再之后找到两个数之和等于sum即可，
这样一来问题又转化为了求two sum，这时候我们一次扫描，找到了等于sum的两数后，
加上当前遍历到的数字，按顺序存入结果中即可，然后还要注意跳过重复数字。
时间复杂度为 O(n2)

'''

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if(nums.size()<3)
            return result;
        sort(nums.begin(),nums.end());
        
        const int target=0;
        auto begin=nums.begin(),last=nums.end()-1;
        for(auto i=begin;i<last-1;i++)
        {
            if(*(i)>0) break;
            if(i>begin&&*(i)==*(i-1)) continue;
            
            auto j=i+1;
            auto k=last;
            while(j<k)
            {
                if(*(i)+*(j)+*(k)<target)
                {
                    j++;
                    while(j<k&&*(j-1)==*(j)) j++;
                }
                else if(*(i)+*(j)+*(k)>target)
                {
                    k--;
                    while(j<k&&*(k+1)==*(k)) k--;
                }
                else
                {
                    result.push_back({*(i),*(j),*(k)});
                    j++;
                    k--;
                    while(*j == *(j - 1) && *k == *(k + 1) && j < k) j++;
                }
            }
        }
        return result;
    }
};