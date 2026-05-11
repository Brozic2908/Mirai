class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        vocab1 = {}
        vocab2 = {}
        
        for i in range(len(s)):
            vocab1[s[i]] = 1 + vocab1.get(s[i], 0)
            vocab2[t[i]] = 1 + vocab2.get(s[i], 0)
        
        return vocab1 == vocab2