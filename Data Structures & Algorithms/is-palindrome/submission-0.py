class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        pointer1 = 0
        pointer2 = len(s) - 1
        while pointer1 < pointer2:
            if s[pointer1] == s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                return False
        return True