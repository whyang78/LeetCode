#方法一
'''
   如果允许O(n log n)的复杂度，那么可以先排序，可是本题要求O(n)。
   由于序列里的元素是无序的，又要求O(n)，首先要想到用哈希表。
   用一个哈希表unordered_ map<int, bool> used 记录每个元素是否使用,对每个元素，以该元
   素为中心，往左右扩张，直到不连续为止，记录下最长的长度。
'''

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,bool> used;
        for(auto i : nums) used[i]=false;
        int longest=0;

        for(auto i : nums)
        {
            if (used[i]) continue;

            int length=1;
            used[i]=true;
            for(int j=i+1;used.find(j)!=used.end();j++)
            {
                used[j]=true;
                length++;
            }
            for(int j=i-1;used.find(j)!=used.end();j--)
            {
                used[j]=true;
                length++;
            }
            longest=max(longest,length);
        }
        return longest;
    }
};

#方法二：
'''
第一直觉是个聚类的操作，应该有union,find 的操作.连续序列可以用两端和长度来表;
示.本来用两端就可以表示， 但考虑到查询的需求，将两端分别暴露出来.用unordered_-
map<int，int> map 来存储.

'''
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        
        unordered_map<int,int> map;
        int length=1;
        for(int i=0;i<nums.size();i++)
        {
            if(map.find(nums[i])!=map.end()) continue;

            map[nums[i]]=1;
            if(map.find(nums[i]-1)!=map.end())
            {
                length=max(length,mergeCluster(map,nums[i]-1,nums[i]));
            }
            if(map.find(nums[i]+1)!=map.end())
            {
                length=max(length,mergeCluster(map,nums[i],nums[i]+1));
            }   
        }
        return length;

    }

private:
    int mergeCluster(unordered_map<int, int> &map, int left, int right)
    {
        int upper=right+(map[right]-1);
        int lower=left-(map[left]-1);
        int length=upper-lower+1;
        map[upper]=length;
        map[lower]=length;
        return length;
    }
};