class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the list
        nums.sort()

        res = []
        

        for i, num in enumerate(nums):

            l, r = i +1, len(nums) -1

            while l < r:

                current_sum = num + nums[l] + nums[r]

                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    if [num, nums[l], nums[r]] not in res:
                        res.append([num, nums[l], nums[r]])
                    l +=1

        return res

