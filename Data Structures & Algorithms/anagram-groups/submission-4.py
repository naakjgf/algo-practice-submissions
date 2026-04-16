class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lengthDict = defaultdict(list)
        
        for word in strs:
            letterCount = [0] * 26
            for char in word:
                letterCount[ord(char) - ord('a')] += 1
            lengthDict[tuple(letterCount)].append(word)
        return lengthDict.values()