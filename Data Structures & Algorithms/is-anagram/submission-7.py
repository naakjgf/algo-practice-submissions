class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        defDict = defaultdict(int)
        for ltr in s:
            defDict[ord('a') - ord(ltr)] += 1
        for ltr in t:
            defDict[ord('a') - ord(ltr)] -= 1
        for value in defDict.values():
            if value != 0:
                return False
        return True