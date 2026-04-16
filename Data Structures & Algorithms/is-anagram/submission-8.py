class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = defaultdict(int)
        for char in s:
            anagram_dict[ord(char)] += 1
        for char in t:
            anagram_dict[ord(char)] -= 1
        for value in anagram_dict.values():
            if value != 0:
                return False
        return True
