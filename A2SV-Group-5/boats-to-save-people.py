class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #time complexity O(N)
        #space complexity O(1)
        if len(people) == 1:
            return 1
        
        left = 0
        right = len(people) - 1
        boat = 0
        
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boat += 1

        return boat