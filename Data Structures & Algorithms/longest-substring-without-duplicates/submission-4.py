class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub_length =  0
        sub_length = 0
        
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                sub_length += 1
                print(s[i])
            longest_sub_length = max(longest_sub_length, sub_length)
        
        return longest_sub_length