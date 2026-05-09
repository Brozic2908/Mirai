class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.remove(temp[i])
            tich = math.prod(temp)
            results.append(tich)
        return results