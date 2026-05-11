class Solution:
    def findMin(self, nums: List[int]) -> int:
        for num in nums.sort().values():
            print(num)

        return 0