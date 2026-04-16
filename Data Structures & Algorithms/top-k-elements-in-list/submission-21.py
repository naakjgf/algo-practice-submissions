class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chars = [[] for _ in range(len(nums))]
        def_dict = defaultdict(int)

        for num in nums:
            def_dict[num] += 1

        for key, value in def_dict.items():
            chars[value - 1].append(key)

        print(len(chars))

        res = []
        for index in range(len(nums) - 1, -1, -1):
            for item in chars[index]:
                res.append(item)
                if len(res) == k:
                    return res
            