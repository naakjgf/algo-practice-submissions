class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countDict = defaultdict(int)

        for letter in s:
            countDict[letter] += 1
        
        for letter in t:
            countDict[letter] -= 1
        
        for value in countDict.values():
            if value != 0:
                return False
        return True