class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set()
        max_length = 0
        left = right = 0

        while right < len(s) - 2:
            length = 0
            while (s[left] == s[right + 1]):
                right += 1
                length += 1
                max_length = max(length, max_length)

            left = right
            while k > 0:
                k -= 1
                right += 1
                length += 1
                max_length = max(length, max_length)
            

        return max_length