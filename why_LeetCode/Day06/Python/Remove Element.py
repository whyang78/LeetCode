'''
解题思路：去掉数组中等于elem的元素，返回新的数组长度，数组中的元素不必保持原来的顺序。
       使用头尾指针，头指针碰到elem时，与尾指针指向的元素交换，将elem都换到数组的末尾去。
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rear=len(nums)-1
        for front in range(len(nums)-1,-1,-1):
            if nums[front]==val:
                nums[front],nums[rear]=nums[rear],nums[front]
                rear-=1
        return rear+1