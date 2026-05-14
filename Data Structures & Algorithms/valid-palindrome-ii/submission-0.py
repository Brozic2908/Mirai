class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            print("1". s[l : r])
            if s[l] != s[r]:
                print(l, r)
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                print(skipL, skipR, r)
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True