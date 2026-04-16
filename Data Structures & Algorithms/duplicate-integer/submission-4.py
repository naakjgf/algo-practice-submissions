class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupDums = set()
        for num in nums:
            if num in dupDums:
               return True
            dupDums.add(num)
        return False