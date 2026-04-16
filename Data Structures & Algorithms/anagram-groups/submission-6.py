class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def_dict = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char) - ord('a')] += 1
            def_dict[tuple(chars)].append(s)
        return def_dict.values()