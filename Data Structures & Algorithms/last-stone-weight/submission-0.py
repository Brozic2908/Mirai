class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            print(stone1, stone2)
            if stone1 > stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))
            elif stone1 < stone2:
                heapq.heappush(max_heap, -(stone2 - stone1))
        
        return -heapq.heappop(max_heap)
        