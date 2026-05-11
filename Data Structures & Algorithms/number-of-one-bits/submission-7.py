class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        print(n)
        return n % 10 + self.hammingWeight(n // 10)