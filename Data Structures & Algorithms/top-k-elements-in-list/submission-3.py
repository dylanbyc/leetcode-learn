class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}
        
        # create a dictionary with frequency
        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        sorted_data = list(dict(sorted(num_dict.items(), key=lambda item: item[1], reverse = True)).keys())

        print(sorted_data)


        return sorted_data[0:k]


        