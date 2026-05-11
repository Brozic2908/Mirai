class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counted = Counter(nums)
        num_sorted = sorted(counted)
        print(counted)
        print(num_sorted)
        results = []
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] - num_sorted[i]:
                results.append(num_sorted[i])
                results.append(num_sorted[i + 1])
        print(results)
        return len(results)