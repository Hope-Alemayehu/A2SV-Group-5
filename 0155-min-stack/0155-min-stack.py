class MinStack:

    def __init__(self):
        self.stack = []
        self.curMin = float("inf")
    def push(self, val: int) -> None:
        if not self.stack:
            self.curMin = val
            self.stack.append([val, self.curMin])
            return
        self.curMin = min(self.curMin, val)
        self.stack.append([val,self.curMin])


    def pop(self) -> None:
        topVal, mini = self.stack.pop()
        if self.stack and mini == self.curMin:
            self.curMin = self.stack[-1][1]

    def top(self) -> int:
        topVal, Mini = self.stack[-1]
        return topVal
        

    def getMin(self) -> int:
        topVal, Mini = self.stack[-1]
        return Mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()