class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub_length =  0
        sub_length = 0
        i = 0
        
        while i < (len(s) - 1):
            current_s = s[i]
            while s[i] != s[i + 1]:
                sub_length += 1
                i += 1
                if current_s == s[i] or i >= len(s) - 1:
                    return longest_sub_length
                print(s[i])
            longest_sub_length = max(longest_sub_length, sub_length)
        
        return longest_sub_length