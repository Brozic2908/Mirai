class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub_length =  0
        sub_length = 0
        i = 0
        current_s = s[i]
        
        while i < (len(s) - 1):
            if current_s == s[i]:
                sub_length = 0
                current_s == s[i + 1]
            if [i] != s[i + 1]:
                sub_length += 1
                print(s[i])
            i += 1
            longest_sub_length = max(longest_sub_length, sub_length)
        
        return longest_sub_length