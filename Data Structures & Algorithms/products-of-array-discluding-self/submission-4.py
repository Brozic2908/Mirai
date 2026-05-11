class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            temp = nums
            temp.pop(i)
            print(temp)