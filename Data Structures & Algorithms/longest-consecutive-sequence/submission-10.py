class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        num_sorted = sorted(nums)
        count = 1
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] - num_sorted[i] == 1:
                count += 1
        return count