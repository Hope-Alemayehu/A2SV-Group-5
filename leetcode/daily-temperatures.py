class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n

        for i,t in enumerate (temperatures):
            while stack and t > stack[-1][1]:
                stackidx ,stackT = stack.pop()
                res[stackidx] = i - stackidx 
            stack.append([i,t])
        return res