class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            elif len(stack) > 0 and ((stack[-1] == "[" and char == "]") or (stack[-1] == "{" and char == "}") or (stack[-1] == "(" and char == ")")):
                stack.pop()
        
        return True if len(stack) == 0 else False