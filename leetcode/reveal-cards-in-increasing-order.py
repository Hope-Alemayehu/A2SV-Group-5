class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #reverse the process
        deck.sort()
        q= deque()
        n = len(deck)
        i = n-1 #start from the end
        while i >= 0:
            if q:
                #moving the end to the front
                tmp = q.pop()
                q.appendleft(tmp)
            #appending the current value to the beginning
            q.appendleft(deck[i])
            i -= 1
        return q