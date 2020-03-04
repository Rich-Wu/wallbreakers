from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for score in ops:
            if score == "+":
                stack.append(stack[-1] + stack[-2])
            elif score == "D":
                stack.append(stack[-1] * 2)
            elif score == "C":
                stack.pop()
            else:
                stack.append(int(score))
        return sum(stack)