class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        for i in range(1, len(asteroids)):
            print(stack)
            ls = stack[-1]
            if ls * asteroids[i] < 0:
                if ls + asteroids[i] < 0:
                    stack.pop()
                    stack.append(asteroids[i])
                elif ls + asteroids[i] == 0:
                    stack.pop()
            else:
                stack.append(asteroids[i])
            print(stack)

        return stack