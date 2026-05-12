class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for ops in operations:
            if ops.isdigit():
                stack.append(int(ops))
            elif ops == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(stack[-1] * 2)

        return sum(stack)