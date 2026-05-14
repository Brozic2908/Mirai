class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        new_list = []

        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                new_list.append(nums[i])
        
        for i in range(len(new_list)):
            nums[i] = new_list[i]

        return count
