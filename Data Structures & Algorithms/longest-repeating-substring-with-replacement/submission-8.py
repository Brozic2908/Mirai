class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set()
        max_length = 0
        left = right = 0

        while right < len(s) - 2:
            length = 0
            c = k
            print(s[left] == s[right + 1])
            while (s[left] == s[right + 1]) and right < len(s) - 2:
                print(s[right])
                right += 1
                length += 1
                max_length = max(length, max_length)
            
            while c > 0:
                print(s[right])
                c -= 1
                length += 1
                max_length = max(length, max_length)

            left = right
            right += 1

        return max_length