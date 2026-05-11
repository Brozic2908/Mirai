class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = nums.copy()
            temp.remove(temp[i])
            tich = math.prod(temp)
            print(tich)
        return []