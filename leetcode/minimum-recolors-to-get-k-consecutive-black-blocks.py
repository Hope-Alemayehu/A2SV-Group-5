class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
       
        count = 0
        for i in range(k):
            if blocks[i] == "W":
                count += 1
        left = 0
        res = count
        for i in range(k, len(blocks)):
            
            
            if blocks[left] == "W":
                count -= 1
            if blocks[i] == "W":
                count += 1
            res = min(res,count)
            left += 1
        return res if res >= 0  else 0
