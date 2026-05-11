class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)
        return list(sorted(num_map.keys(), reverse=True))