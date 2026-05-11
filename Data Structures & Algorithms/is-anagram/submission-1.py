class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab1 = []
        for i in range(len(s)):
            vocab1[s[i]] = 0
            vocab2[t[i]] = 0
        
        for i in range(len(s)):
            vocab1[s[i]] += 1
            vocab2[t[i]] += 1
        
        return vocab1 == vocab2