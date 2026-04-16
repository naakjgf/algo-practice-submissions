class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, num in enumerate(nums):
            if num in sum_dict:
                return [sum_dict[num], i]
            sum_dict[target - num] = i 

        return []