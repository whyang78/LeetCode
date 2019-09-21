class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        rfirst=len(nums)-1
        rlast=-1
        
        pivot=rfirst-1
        while pivot!=rlast and nums[pivot]>=nums[pivot+1]:
            pivot-=1
        
        if pivot==rlast:
            nums.sort()
            return
        
        for i in range(rfirst,-1,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        nums[pivot+1:len(nums)]=nums[pivot+1:len(nums)][::-1]
        return