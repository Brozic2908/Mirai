class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []

        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            heapq.heappush(min_heap, (num, right))
            heapq.heappush(max_heap, (-num, right))

            while - max_heap[0][0] - min_heap[0][0] > limit:
                left += 1

                while(max_heap[0][1] < left):
                    heapq.heappop(max_heap)
                while(min_heap[0][1] < left):
                    heapq.heappop(min_heap)
            
            max_length = max(max_length, right - left + 1)

        return max_length