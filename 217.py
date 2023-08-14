class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        elems = set()
        for i in nums:
            if i in elems:
                return True
            else:
                elems.add(i)
        return False