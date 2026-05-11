class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest_sub_length =  0
        left = 0
        right = 1
        
        while right < len(s) - 1:
            if s[right] == s[right -  1] and s[left] == s[right]:
                left = right
            print(s[left], s[right])
            longest_sub_length = max(longest_sub_length, right - left - 1)
            right += 1
        return longest_sub_length