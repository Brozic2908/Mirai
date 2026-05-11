class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            print((left, mid, right))

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid

        return -1 