class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) == 1:
            return -1
        hashi = defaultdict(int)
        res = float("inf")
        left = 0
        for i in range(len(cards)):
            hashi[cards[i]] += 1 
            
            while hashi[cards[i]] == 2:
                res = min(res, i - left + 1) 
                hashi[cards[left]] -= 1
                left += 1
                if hashi[cards[i]] < 2:
                    break
        return res if res != float("inf") else -1  
        

