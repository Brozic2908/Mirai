class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            num_map[i] = 1 + num_map.get(i, 0)
        