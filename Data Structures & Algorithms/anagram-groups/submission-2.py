class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        results = []
        for i in range(len(strs)):
            if Counter(strs[i]) in ana_map.value():
                results.append(strs[i])
            ana_map[i] = Counter(strs[i])
        
        for key, values in results:
            print(key, values)