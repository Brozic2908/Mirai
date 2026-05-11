class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 1: return 0
        return n % 10 + self.hammingWeight(n // 10)