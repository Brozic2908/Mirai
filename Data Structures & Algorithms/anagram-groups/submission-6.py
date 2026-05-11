class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for i in range(len(strs)):
            results[tuple(sorted(strs[i]))].append(strs[i])
        
        for k, v in range(results):
            print(k)
            print(v)