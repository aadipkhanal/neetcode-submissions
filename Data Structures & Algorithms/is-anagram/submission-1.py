class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(h):
            help_dict = {}
            for item in h:
                if item not in help_dict:
                    help_dict[item] = 1
                else:
                    help_dict[item]+=1
            return help_dict
        if helper(s) == helper(t):
            print(helper(s))
            print(helper(t))
            return True
        else:
            return False
        