//方法一：使用异或
//时间复杂度：O(N) 空间复杂度:O(1)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result=0;
        for(auto num : nums)
        {
            result^=num;
        }
        return result;
    }
};

//方法二：使用异或
//时间复杂度：O(N) 空间复杂度:O(1)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return accumulate(nums.begin(),nums.end(),0,bit_xor<int>());
    }
};