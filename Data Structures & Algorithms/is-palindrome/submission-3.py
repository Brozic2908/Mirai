class Solution:
    def convert_to_str(self, s: str) -> str:
        # return re.sub(r"^a-z0-9","", s.lower())
        return "".join(char.lower() for char in s if char.isalnum())
    
    def isPalindrome(self, s: str) -> bool:
        s = self.convert_to_str(s)
        head = 0
        fail = len(s) - 1
        print(len(s))
        print(s[fail])
        return True