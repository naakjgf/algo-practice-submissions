class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
        while a < b:
            curSum = numbers[a] + numbers[b]
            if (curSum == target): return [a + 1, b + 1]
            if (curSum < target): a += 1
            if (curSum > target): b -= 1
