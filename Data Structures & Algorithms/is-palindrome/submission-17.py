class Solution:    
    def isPalindrome(self, s: str) -> bool:
        context = s.split(" ")
        left = 0
        right = len(context) - 1
        while left < right:
            if self.checkAlNum(context[left]) != self.checkAlNum(context[right]):
                return False
            left += 1
            right -= 1
        return True
            

    def checkAlNum(self, s: str):
        return re.sub(r"[^A-Za-z0-9]", "", s)