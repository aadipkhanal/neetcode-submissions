class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return True
            my_dict[num] = i
        return False
         