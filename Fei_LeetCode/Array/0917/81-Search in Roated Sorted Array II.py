# 正确做法应该采用二分法
def search(self, nums: list[int], target: int) -> bool:
    if target in nums:
        return True
    else:
        return False
