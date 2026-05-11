class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums.sort().get(0)