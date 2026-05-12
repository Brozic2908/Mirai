class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        stack.append(asteroids[0])
        for i in range(1, len(asteroids)):
            # ls = stack[-1]
            # if ls * asteroids[i] < 0:
            #     if ls < asteroids[i]:
            #         stack.pop()
            #     else:
            #         stack.append(asteroids)
            print(stack)
        return [stack.pop()]