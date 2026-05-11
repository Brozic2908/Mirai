class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest_sub_length =  1
        i = 0
        current_s = i
        
        while i < len(s) - 1:
            if s[current_s] == s[i] and i != current_s:
                current_s = i

            if s[i] != s[i + 1]:
                current_s += 1
                print(current_s)
                print(s[i], s[i + 1])
            else:
                current_s = i

            print(longest_sub_length, current_s)
            longest_sub_length = max(longest_sub_length, current_s)
            i += 1
        
        return longest_sub_length