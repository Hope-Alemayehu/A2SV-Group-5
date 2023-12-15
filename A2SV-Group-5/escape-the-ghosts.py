class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        #by calculating the amount of step the ghosts take to get to target
        #and by calculating the amount of steps the player initally at [0,0] to the target .
        #return True if the steps of player<steps of Ghosts
        #return False the steps of Ghosts
        #time complexity = O(N)
        #space complexity = O(1)


        d=abs(target[0])+abs(target[1])

        for ghost in ghosts:
            distance=abs(target[0]-ghost[0])+abs(target[1]-ghost[1])

            if distance<=d:
                return False
        return True 