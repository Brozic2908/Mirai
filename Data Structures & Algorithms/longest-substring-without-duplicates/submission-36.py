class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest_sub_length =  1
        sub_length = 1
        i = 0
        current_s = i
        
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                sub_length += 1
                print(s[i], s[i + 1])
            else:
                sub_length = 1
                current_s = i

            
            if s[current_s] == s[i]:
                sub_length = 1
                current_s = i

            i += 1
            longest_sub_length = max(longest_sub_length, sub_length)
        
        return longest_sub_length