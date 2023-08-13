class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        leading_num = nums[0]
        for i in nums:
            if i == leading_num:
                count += 1
            else:
                count -= 1
            if count == 0:
                leading_num = i
                count += 1
        return leading_num