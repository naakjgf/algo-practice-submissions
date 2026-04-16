class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, longest_subarray = 0, 0
        counts = defaultdict(int)

        for R in range(0, len(s)):
            counts[s[R]] += 1
            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            
            longest_subarray = max(R - L + 1, longest_subarray)
        
        return longest_subarray