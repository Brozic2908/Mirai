class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        pq = []
        carry = 0
        max_queue = 0

        for num in nums:
            heapq.heappush(pq, num)
            carry = abs(max(pq) - min(pq))
            if carry > limit:
                while(len(pq) != 0):
                    pq.pop()
            max_queue = len(pq)
        
        print(pq)
        return max_queue