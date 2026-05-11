class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        head = 0
        tail = len(heights) - 1

        while head < tail:
            width = heights[tail] - heights[head]
            height = min(heights[head], heights[tail])
            
            water = width * height
            max_water = max(water, max_water)
            
            head += 1
            tail -= 1
            while heights[head] <= heights[head - 1]:
                head += 1
            while heights[tail] >= heights[tail + 1]:
                tail += 1
        
        return max_water