class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == 0 or len(t) > len(s): return ""

        need_map = {}
        for need_s in t:
            need_map[need_s] = need_map.get(need_s, 0) + 1
        
        for k, v in need_map.items():
            print(k, v)

        # for sub_s in s:        
            # context_window += ""
            

        return ""