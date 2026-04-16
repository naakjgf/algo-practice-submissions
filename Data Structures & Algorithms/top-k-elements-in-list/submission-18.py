class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chars = [[] for _ in range(len(nums) + 1)]
        def_dict = defaultdict(int)

        for num in nums:
            def_dict[num] += 1

        for key, value in def_dict.items():
            chars[value].append(key)

        res = []
        for index in range(len(chars) - 1, 0, -1):
            for item in chars[index]:
                res.append(item)
                if len(res) == k:
                    return res
            if len(res) == k:  # Double-check after inner loop
                return res
            