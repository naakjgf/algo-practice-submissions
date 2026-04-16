class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_nums = []
        for i in range(len(nums)):
            nums_dupe = nums.copy()
            nums_dupe[i] = 1
            product = 1
            for num in nums_dupe:
                product *= num
            return_nums.append(product)
        return return_nums