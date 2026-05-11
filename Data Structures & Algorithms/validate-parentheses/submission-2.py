class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ["[", "{", "("]:
                stack.append(char)
            elif (stack[-1] == "[" and char == "]") or (stack[-1] == "{" and char == "}") or (stack[-1] == "(" and char == ")"):
                stack.pop()
        
        return True if len(stack) else False