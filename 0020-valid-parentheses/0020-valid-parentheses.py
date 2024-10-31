class Solution:
    def isValid(self, s: str) -> bool:
        #time complexity O(N)
        #space complexity O(N)
        bracket_map = {"}":"{",")":"(","]":"["}
        stack = []

        for c in s:
            if c in bracket_map and stack and stack[-1] == bracket_map[c]:
                stack.pop()
                continue
            stack.append(c)
        return len(stack) == 0

        