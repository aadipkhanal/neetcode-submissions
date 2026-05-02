class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        char_count2 = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in t:
            if char in char_count2:
                char_count2[char] += 1
            else:
                char_count2[char] = 1
        return char_count == char_count2
        
