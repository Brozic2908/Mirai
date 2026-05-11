class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        pq = []
        carry = 0

        for num in nums:
            heapq.heappush(pq, num)
            carry = abs(max(pq) - min(pq))
            if carry > limit:
                pq.pop()

        
        print(pq)
        return len(pq)