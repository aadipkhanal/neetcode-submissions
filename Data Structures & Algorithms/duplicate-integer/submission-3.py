class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_arr = []
        for num in nums:
            if num in new_arr:
                return True
            new_arr.append(num)
        return False