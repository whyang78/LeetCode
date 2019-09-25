//时间：2019-9-19
//作者：fish_bot
//题目：LeetCode 1


//hash表，key为数字，value为位置
//map.find()返回一个迭代器，找不到时返回map.end()
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int,int> map;
        vector<int> result;
        
        for (int i = 0; i < nums.size(); i++)
        {
            map[nums[i]]=i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int temp = target - nums[i];
            if(map.find(temp) != map.end() && map[temp] > i)
            {
                result.push_back(i);
                result.push_back(map[temp]);
            }
        }
        return result;
    }
};


