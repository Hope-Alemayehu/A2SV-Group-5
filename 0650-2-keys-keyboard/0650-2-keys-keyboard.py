class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        q = deque([(1, 0, 0)])  
        v = set((1, 0))  
        while q:
            a, b, c = q.popleft()
            if a == n: return c
            if a > 0 and (a, a) not in v:
                q.append((a, a, c + 1))
                v.add((a, a))
            if b > 0 and a + b <= n:
                if (a + b, b) not in v:
                    q.append((a + b, b, c + 1))
                    v.add((a + b, b))
        return -1