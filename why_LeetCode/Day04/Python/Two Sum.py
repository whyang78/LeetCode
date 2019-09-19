class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict={}
        for i,num in enumerate(nums):
            another=target-num
            if another in nums_dict.keys() and nums_dict[another]!=i:
                return [i,nums_dict[another]]
            nums_dict[num]=i