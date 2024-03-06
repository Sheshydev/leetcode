class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            j = mem.get(num, None)
            if j is not None:
                break
            mem[target - num] = i

        return [i,j]

