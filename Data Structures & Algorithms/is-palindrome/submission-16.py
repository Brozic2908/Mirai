class Solution:
    def convert_to_str(self, s: str) -> str:
        # return re.sub(r"^a-z0-9","", s.lower())
        return "".join(char.lower() for char in s if char.isalnum())
    
    def isPalindrome(self, s: str) -> bool:
        aln = self.convert_to_str(s)
        if len(aln) == 1 or len(aln) == 0: return True
        head = 0
        tail = len(aln) - 1
        while(head < tail):
            if aln[head] != aln[tail]: return False
            head += 1
            tail -= 1
        return True