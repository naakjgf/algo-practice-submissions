class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lengthDict = defaultdict(list)
        solution = []

        for string in strs:
            sorted_string = ''.join(sorted(string))
            lengthDict[sorted_string].append(string)

        return lengthDict.values()