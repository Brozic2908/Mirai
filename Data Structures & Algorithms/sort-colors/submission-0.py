class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.heapSort(nums)
        return nums
    
    def heapify(self, nums, n, i):
        largest = i
        left = (i << 1) + 1
        right = (i << 1) + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        
        if right < n and nums[right] > nums[largest]:
            largest = right
        
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, n, largest)
        
    
    def heapSort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)