//时间：2019-9-17
//作者：fish_bot
//题目：LeetCode 81

class Solution {
public:
	bool search(vector<int>& nums, int target)
	{
		int len = nums.size();

		int head = 0;
		while (head != len) {
			int mid = (head + len) / 2;
			if (nums[mid] == target)
				return true;
			if (nums[head] == nums[mid])//
			{
				head++;
			}
			else if (nums[head] < nums[mid])
			{
				if (target < nums[mid] && target >= nums[head])
					len = mid;
				else
					head = mid + 1;
			}

			else
			{
				if (target > nums[mid] && target <= nums[len - 1])
					head = mid + 1;
				else
					len = mid;
			}
		}

		return false;
	}
};


//与33题思路基本一致，判断一下head和mid相等的情况，如果相等就head++，这一步时间复杂度为O（n）