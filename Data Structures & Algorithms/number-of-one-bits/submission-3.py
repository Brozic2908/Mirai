class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        num = n % 10
        return num + self.hammingWeight(n // 10)