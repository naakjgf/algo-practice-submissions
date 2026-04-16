class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeSet = set()

        for num in nums:
            if num in dupeSet:
                return True
            dupeSet.add(num)
        return False
        # return len(nums) != len(set(nums))