class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        def anagram(word: str) -> str:
            return ''.join(sorted(word))

        for word in strs:
            signature = anagram(word)
            if signature not in anagram_dict:
                anagram_dict[signature] = []
            anagram_dict[signature].append(word)

        return list(anagram_dict.values())
                
                