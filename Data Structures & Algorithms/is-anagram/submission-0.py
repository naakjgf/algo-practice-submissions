class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tList = list(t)
        for letter in s:
            if letter not in tList:
                return False
            tList.remove(letter)
        return True