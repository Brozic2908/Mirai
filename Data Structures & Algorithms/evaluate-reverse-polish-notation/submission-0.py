def is_int(num: int) -> bool:
    try:
        int(s)
        return True
    except ValidError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            print(stack)
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                num1 = stack.pop()
                stack.append(stack.pop() / num1)
            else:
                stack.append(int(token))
        
        return stack[0]