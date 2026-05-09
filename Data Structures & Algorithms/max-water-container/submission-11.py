class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        head = 0
        tail = n - 1

        while head < tail:
            width = tail - head
            height = min(heights[head], heights[tail])

            water = width * height
            max_water = max(water, max_water)
            
            # Chỉ di chuyện cột thấp hơn
            if heights[head] < heights[tail]:
                head += 1
            else: 
                tail -= 1

        return max_water