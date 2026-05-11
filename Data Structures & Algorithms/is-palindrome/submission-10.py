class Solution:
    def convert_to_str(self, s: str) -> str:
        # return re.sub(r"^a-z0-9","", s.lower())
        return "".join(char.lower() for char in s if char.isalnum())
    
    def isPalindrome(self, s: str) -> bool:
        aln = self.convert_to_str(s)
        head = 0
        fail = len(aln) - 1
        print(len(aln))
        print(aln[fail])
        return True