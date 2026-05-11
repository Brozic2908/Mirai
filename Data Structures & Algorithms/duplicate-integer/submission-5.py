class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            print("i = ", i)
            for j in range(len(nums) - 1):
                if nums[i] == nums[j + 1]:
                    print("j = ", j)
                    return True
        return False