class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):

            gap = target - n

            if gap in seen:
                return [seen[gap], i]

            seen[n] = i

        