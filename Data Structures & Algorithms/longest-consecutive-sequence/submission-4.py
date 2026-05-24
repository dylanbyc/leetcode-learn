class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0

        for num in nums:
            # at the start of the sequence,
            # num -1 must not be in nums
            if num -1 in nums:
                continue
            else:
                length = 1
                while num + 1 in nums:
                    length += 1
                    num += 1

                res = max(res, length)

        return res
        