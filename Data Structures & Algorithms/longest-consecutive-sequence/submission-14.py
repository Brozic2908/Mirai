class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        counted = Counter(nums)
        num_sorted = sorted(counted, key=lambda x: counted[x])
        print(counterd)
        print(num_sorted)
        count = 1
        need_sum = 1
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] == num_sorted[i]:
                need_sum += 1
            elif num_sorted[i + 1] - num_sorted[i] == 1:
                count += need_sum
                need_sum = 1
        return count