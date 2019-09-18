
//方法一 类似于之前的二分查找，但是无法判断相等的情况
class Solution {
public:
    bool search(vector<int>& nums, int target) {
    int first=0,last=nums.size();
    while(first!=last)
    {
        const int mid=(first+last)/2;
        if (nums[mid]==target)
            return true;
        
        if(nums[first]<nums[mid])
        {
            if(nums[first]<=target&&target<nums[mid])
                last=mid;
            else
                first=mid+1;
        }
        else if(nums[first]>nums[mid])
        {
            if(nums[mid]<target&&target<=nums[last-1])
                first=mid+1;
            else
                last=mid;
        }
        //若相等的话，表示出现重复元素，则跳过。
        else
        {
            first++;
        }    
    }
    return false;
    }
};

//方法二 与方法一时间差不多，因为时间复杂度都是O(n)
class Solution {
public:
    bool search(vector<int>& nums, int target) {
       for(int i=0;i<nums.size();i++)
       {
           if(nums[i]==target)
               return true;  
       }
        return false;
    }
};
