class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #time complexity O(NlogN)
        #space complexity O(1)
        
        count = 0
        up = 0
        down = 0

        g.sort()
        s.sort()

        while up < len(g) and down< len(s):
            if s[down] >= g[up]:
                up += 1
                count += 1
            down +=1
        return count
