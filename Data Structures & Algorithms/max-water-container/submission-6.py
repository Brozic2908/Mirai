class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        head = 0
        tail = n - 1

        while head < tail:
            width = tail - head
            height = min(heights[head], heights[tail])
            print(f"height={height}, width={width}")

            water = width * height
            max_water = max(water, max_water)
            
            head += 1
            tail -= 1
            while heights[head] <= heights[head - 1]:
                if head < tail: head += 1
                else: break
            while heights[tail] >= heights[tail + 1]:
                if head < tail: tail -= 1
                else: break
        
        return max_water