class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(","}":"{","]":"["}
        stack = []
        if s[0] in valid.keys():
            return False
        for c in s:
            if c in valid.keys():
                if stack:
                    top = stack[-1]
                    if valid[c] != top:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True