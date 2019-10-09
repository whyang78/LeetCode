class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result=0
        min_gap=sys.maxsize
        nums.sort()
        
        for i in range(len(nums)-2):
            j=i+1;
            k=len(nums)-1
            
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                gap=abs(total-target)
                if gap<min_gap:
                    min_gap=gap
                    result=total
                if total<target:
                    j+=1
                elif total>target:
                    k-=1
                else:
                    return total
        return result