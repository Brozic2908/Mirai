class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        counted = Counter(nums)
        num_sorted = sorted(counted)
        print(counted)
        print(num_sorted)
        count = 0
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] - num_sorted[i] == 1:
                count += counted[num_sorted[i + 1]]
        return count