class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        mid = p1 + ((p2 - p1) // 2)

        while p1 <= p2:
            if target > nums[mid]:
                p1 = mid + 1
            elif target < nums[mid]:
                p2 = mid - 1
            else:
                return mid
            mid = p1 + ((p2 - p1) // 2)
        
        return -1
    
