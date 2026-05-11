class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        mid = round(right / 2, 0)