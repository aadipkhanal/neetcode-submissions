class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        empty_dict_s = {}
        empty_dict_t = {}
        for char in s:
            if char not in empty_dict_s:
                empty_dict_s[char] = 1
            else:
                empty_dict_s[char] += 1
        for char in t:
            if char not in empty_dict_t:
                empty_dict_t[char] = 1
            else:
                empty_dict_t[char] += 1
        if empty_dict_s == empty_dict_t:
            return True
        return False
