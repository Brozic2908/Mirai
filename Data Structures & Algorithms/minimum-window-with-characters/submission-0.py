class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_set = t.set()
        print(type(target_set))