class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in num_and_index:
                return [num_and_index[complement], i]
            else:
                num_and_index[num] = i