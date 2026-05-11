class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0
        max_frequent_char = 0
        
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            max_frequent_char = max(max_frequent_char, count[char])

            window_length = right - left + 1
            
            if window_length - max_frequent_char > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            
            max_length = max(window_length, max_length)
        
        return max_length
