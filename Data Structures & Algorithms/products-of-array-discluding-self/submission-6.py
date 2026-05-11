class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = nums
            temp.remove(temp[i])
            print(temp)