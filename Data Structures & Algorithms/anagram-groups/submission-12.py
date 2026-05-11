class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for i in range(len(strs)):
            results[tuple(sorted(strs[i]))].append(strs[i])
        
        for k, v in results.items():
            print(k)
            # print(v)