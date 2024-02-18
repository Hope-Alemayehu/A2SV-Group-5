class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        thelist = path.split("/")
        print(thelist)
        for c in thelist:
            if c == "" or c == ".":
                continue
            elif c == ".." and stack:
                stack.pop()
            elif  c == ".."  and not stack:
                continue
            else:
                stack.append(c)
        return "/"+"/".join(stack)