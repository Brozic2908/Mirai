class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        results = nums
        for num in results:
            num -= limit
        
        count = 0
        for num in results:
            if num > 0: count += 1
        
        return count