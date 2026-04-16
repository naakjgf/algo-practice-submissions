class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapped = {}
        for num in nums:
            mapped[num] = mapped.get(num, 0) + 1
            if mapped[num] > 1:
                return True
        return False