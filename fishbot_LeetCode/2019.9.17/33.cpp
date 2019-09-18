//时间：2019-9-16
//作者：fish_bot
//题目：LeetCode 33




class Solution {
public:
	int search(vector<int>& nums, int target)
	{
		int len = nums.size();

		int head = 0;
		while (head != len) {
			int mid = (head + len) / 2;//偶数取后一个为中值
			if (nums[mid] == target)
				return mid;
			if (nums[head] <= nums[mid])
			{
				if (target < nums[mid] && target >= nums[head])
					len = mid;
				else
					head = mid + 1;//根据中值计算特点来定是mid+1还是-1
			}

			else
			{
				if (target > nums[mid] && target <= nums[len - 1])
					head = mid + 1;
				else
					len = mid;
			}
		}

		return -1;
	}
};

//注意有序数组，只转一次
//二分法，根据中值与两端值的对比判断旋转位置
//共四种情况
//前半无旋转（target在前 or 在后）
//后半无旋转（target在后 or 在前）
