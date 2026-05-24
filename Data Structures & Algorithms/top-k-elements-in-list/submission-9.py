class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        # sort the dictionary by value
        return [i[0] for i in sorted(
            counter.items(), 
            key = lambda x: x[1], 
            reverse = True)[0:k]]

        


        