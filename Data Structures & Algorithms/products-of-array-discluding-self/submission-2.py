class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = nums
        for i in range(len(nums)):
            temp.pop(i)
            print(temp)