class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sorted = sorted(nums)
        count = 0
        for i in range(len(num_sorted) - 2):
            if num_sorted[i + 1] - num_sorted[i] == 1 or num_sorted[i + 1] == num_sorted[i + 2]:
                count += 1
        return count