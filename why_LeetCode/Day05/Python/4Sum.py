#类似于c++的第二种方法
#不允许重复->set   哈希表->dict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        
        result=set()
        dic={}
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                dic.setdefault(nums[i]+nums[j],[]).append([i,j])
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                gap=target-nums[i]-nums[j]
                if gap in dic.keys():
                    for k in dic[gap]:
                        if k[1]<i:
                            result.add((nums[k[0]],nums[k[1]],nums[i],nums[j]))
        return [list(i) for i in result]