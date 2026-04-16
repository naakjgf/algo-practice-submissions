class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "Empty"
        string = "<!>".join(strs)
        return string

    def decode(self, s: str) -> List[str]:
        if s == "Empty":
            return []
        strs = s.split("<!>")
        print(strs)
        return strs
