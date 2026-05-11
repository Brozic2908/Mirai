class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        head = 0
        tail = n - 1

        while head < tail:
            width = heights[tail] - heights[head]
            height = min(heights[head], heights[tail])
            
            water = width * height
            max_water = max(water, max_water)
            
            head += 1
            tail -= 1
            while heights[head] <= heights[head - 1]:
                if head < tail: head += 1
            while heights[tail] >= heights[tail + 1]:
                if head < tail: tail -= 1
        
        return max_water