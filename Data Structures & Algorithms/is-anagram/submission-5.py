class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = defaultdict(int)

        for letter in s:
            dictionary[letter] += 1
        
        for letter in t:
            dictionary[letter] -= 1
        
        for value in dictionary.values():
            if value != 0:
                return False
        return True