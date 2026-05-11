class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub_length =  0
        sub_length = 0
        
        for i in range(length(s) - 1):
            if s[i] < s[i + 1]:
                print(s[i])