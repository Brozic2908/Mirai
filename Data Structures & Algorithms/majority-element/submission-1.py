class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        max_count = -1000
        i = 0
        for key, value in num_count.items():
            if max_count < value: 
                max_count = value
                i = key

        return i