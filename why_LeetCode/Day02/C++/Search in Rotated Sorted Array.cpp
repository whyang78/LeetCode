    //采用二分查找可以满足复杂度的要求，但列表并非有序。

    //如果中位数比左边大，说明左边是递增的，断点在右边：
    //如果target在左边递增的区间，就在左边查找；否则，在右边查找.

    //如果中位数比左边小，说明右边是递增的，断点在左边：
    //如果target在右边的递增区间，就在右边查找；否则，在左边查找。

class Solution {
public:
    int search(vector<int>& nums, int target) {
    int first=0,last=nums.size();  
    while(first!=last)
    {
        const int mid=(first+last)/2;
        if (nums[mid]==target)
            return mid;
        
	//左边有序
        if(nums[first]<=nums[mid])
        {
            if(nums[first]<=target&&target<nums[mid])
                last=mid;
            else
                first=mid+1;
        }
        //右边有序
        else
        {
            if(nums[mid]<target&&target<=nums[last-1])
                first=mid+1;
            else
                last=mid;
        }
        
    }
    return -1;
    }
};