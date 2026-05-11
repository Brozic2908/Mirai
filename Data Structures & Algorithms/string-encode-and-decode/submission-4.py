class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        results = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                length = int(s[i:j])
                results.append(s[j+2:j+2+length])
                i = j+2+length+1
        return results
