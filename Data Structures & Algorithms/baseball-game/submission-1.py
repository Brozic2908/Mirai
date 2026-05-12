class Solution:
    def calPoints(self, operations: List[str]) -> int:
        for ops in operations:
            if isnum(ops):
                print(ops)
        
        return