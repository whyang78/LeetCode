class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;
        
        length=len(height)
        ans=0
        max_left,max_right=[0]*length,[0]*length
        
        max_left[0]=height[0]
        max_right[length-1]=height[length-1]
        for i in range(1,length):
            max_left[i]=max(max_left[i-1],height[i])
            max_right[length-i-1]=max(max_right[length-i],height[length-i-1])
        for i in range(length):
            ans+=min(max_left[i],max_right[i])-height[i]
        return ans