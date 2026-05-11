class Solution:
    def countBits(self, n: int) -> List[int]:
        print(n)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + 1

        return dp