class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        counted = Counter(nums)
        num_sorted = sorted(counted)
        print(counted)
        print(num_sorted)
        if len(num_sorted) == 1: return 1
        results = []
        streak = 0
        longest_streak = 0
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] - num_sorted[i] == 1:
                results.append(num_sorted[i])
                results.append(num_sorted[i + 1])
                streak = len(set(results))
            else:
                streak = 0
                result.clear()
            if longest_streak < streak:
                longest_streak = streak
        return longest_streak