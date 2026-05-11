class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = nums
            del temp[i]
            print(temp)