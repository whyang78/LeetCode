'''
方法一：两遍哈希表 O(n) 
使用了两次迭代。在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]）
是否存在于表中。注意，该目标元素不能是 nums[i]本身！

'''

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
        vector<int> result;

        for(int i=0;i<nums.size();i++)
        {
            map[nums[i]]=i;
        }

        for(int i=0;i<nums.size();i++)
        {
            int another=target-nums[i];
            if(map.find(another)!=map.end()&&map[another]!=i)
            {
                result.push_back(i);
                result.push_back(map[another]);
                break;
            }
        }
        return result;
    }
};

'''
方法二：一遍哈希表
在进行迭代并将元素插入到表中的同时，检查表中是否已经存在当前元素所对应的目标元素。
如果它存在，那我们已经找到了对应解，并立即将其返回。
'''
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
        vector<int> result;

        for(int i=0;i<nums.size();i++)
        {
            int another=target-nums[i];
            if(map.find(another)!=map.end()&&map[another]!=i)
            {
                result.push_back(i);
                result.push_back(map[another]);
                break;
            }
            map[nums[i]]=i;
        }
        return result;
    }
};