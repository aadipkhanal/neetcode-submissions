class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value_dict = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in index_value_dict:
                return [index_value_dict[complement], i]
            index_value_dict[num] = i
