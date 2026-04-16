class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}#{word}"
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            strings.append(s[j + 1: j + word_length + 1])
            i = j + word_length + 1
        return strings
