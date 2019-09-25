//时间：2019-9-23
//作者：fish_bot
//题目：LeetCode 27




class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int res = 0;
        for(int i = 0; i < len; i++){
            if(nums[i] != val){
                nums[res] = nums[i];
                res++;
                
            }   
        }
        return res;
    }
};